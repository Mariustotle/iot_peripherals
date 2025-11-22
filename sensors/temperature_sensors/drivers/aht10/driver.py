from typing import Dict, Optional
from time import sleep
from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_position import PinPosition
import smbus2

from peripherals.contracts.temperature_measurement import TemperatureMeasurement
from peripherals.sensors.temperature_sensors.config.digital_i2c_config import DigitalI2CTemperatureConfig
from peripherals.sensors.temperature_sensors.driver_base import TemperatureDriverBase
from peripherals.sensors.temperature_sensors.response import DigitalTempResponse


class AHT10(TemperatureDriverBase):
    """
    AHT10 Temperature + Humidity Sensor (High Precision I2C)
    Datasheet formulas implemented:
        - Humidity:     RH = (S_rh / 2^20) * 100
        - Temperature:  T = ((S_t / 2^20) * 200) - 50
    """
    DEFAULT_I2C_ADDR:int = 0x38 # 0x38 = 56 in hex notation
    DEFAULT_BUS_NUMBER:int = 1

    i2c_addr:int = None
    i2c_bus_number:int = None
    bus: Optional[smbus2.SMBus] = None    


    def __init__(self, config:DigitalI2CTemperatureConfig, simulated:bool = False, pins:Optional[Dict[PinPosition, PinDetails]] = None):
        super().__init__(config, simulated, pins)
        self.bus: Optional[smbus2.SMBus] = None
        self.i2c_addr = config.i2c_address if config.i2c_address else self.DEFAULT_I2C_ADDR
        self.i2c_bus_number = config.channel if config.channel else self.DEFAULT_BUS_NUMBER      

        self.initialized = False


    # ----------------------------------------------------------
    # INITIALIZATION
    # ----------------------------------------------------------
    def _initialize(self, name: str, config: Optional[DigitalI2CTemperatureConfig] = None) -> bool:

        # Open bus
        try:
            self.bus = smbus2.SMBus(self.i2c_bus_number)
        except Exception as ex:
            raise RuntimeError(f"AHT10: Failed to open I2C bus {self.i2c_bus_number}: {ex}")

        # SOFT RESET
        try:
            self.bus.write_byte(self.i2c_addr, 0xBA)  # Soft reset command
            sleep(0.02)
        except Exception as ex:
            raise RuntimeError(f"AHT10: Soft reset failed: {ex}")

        # INITIALIZE & CALIBRATE SENSOR
        # Command: 0xE1, param1=0x08, param2=0x00
        try:
            self.bus.write_i2c_block_data(self.i2c_addr, 0xE1, [0x08, 0x00])
            sleep(0.01)
        except Exception as ex:
            raise RuntimeError(f"AHT10: Initialization command failed: {ex}")

        self.initialized = True
        return True


    # ----------------------------------------------------------
    # RAW READING
    # ----------------------------------------------------------
    def read_raw(self):
        """
        Perform a measurement and return temperature (°C) and humidity (%RH)
        """

        if not self.initialized:
            raise RuntimeError("AHT10: read_raw() called before initialization")

        # Trigger measurement
        try:
            self.bus.write_i2c_block_data(self.i2c_addr, 0xAC, [0x33, 0x00])
        except Exception as ex:
            raise RuntimeError(f"AHT10: Failed to trigger measurement: {ex}")

        sleep(0.1)  # Measurement delay per datasheet (max 75ms)

        # Read 6 bytes of measurement data
        try:
            data = self.bus.read_i2c_block_data(self.i2c_addr, 0x00, 6)
        except Exception as ex:
            raise RuntimeError(f"AHT10: Failed to read data: {ex}")

        # Data format:
        # Byte0: status
        # Byte1-2-3: humidity (20 bits)
        # Byte3-4-5: temperature (20 bits)

        # Extract humidity bits (20-bit)
        raw_humidity = ((data[1] << 12) |
                        (data[2] << 4) |
                        (data[3] >> 4))

        # Extract temperature bits (20-bit)
        raw_temp = (((data[3] & 0x0F) << 16) |
                    (data[4] << 8) |
                    data[5])

        # Convert per datasheet
        humidity = (raw_humidity / 1048576.0) * 100.0
        temperature = ((raw_temp / 1048576.0) * 200.0) - 50.0

        return temperature, humidity


    # ----------------------------------------------------------
    # PUBLIC READ API (USED BY YOUR FRAMEWORK)
    # ----------------------------------------------------------
    def _default_reading(self):

        temperature, humidity = self.read_raw()

        # Fahrenheit conversion if configured
        if temperature is not None:
            if self.config.measurement == TemperatureMeasurement.Fahrenheit:
                temperature = (temperature * 9/5) + 32

        return DigitalTempResponse.create(
            temperature=temperature,
            measurement=self.config.measurement,
            humidity=humidity
        )


    # ----------------------------------------------------------
    # CLEANUP
    # ----------------------------------------------------------
    def cleanup(self):
        if self.bus:
            try:
                self.bus.close()
            except:
                pass
            self.bus = None
