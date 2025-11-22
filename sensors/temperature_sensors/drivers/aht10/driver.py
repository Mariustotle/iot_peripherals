from typing import Optional
from time import sleep
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
    DEFAULT_I2C_ADDR = 0x38

    def __init__(self):
        super().__init__()
        self.bus: Optional[smbus2.SMBus] = None
        self.i2c_addr = self.DEFAULT_I2C_ADDR
        self.i2c_bus_number = 1  # Default for Raspberry Pi 3/4/5

        self.initialized = False


    # ----------------------------------------------------------
    # INITIALIZATION
    # ----------------------------------------------------------
    def _initialize(self, name: str, config: Optional[DigitalI2CTemperatureConfig] = None) -> bool:

        # I2C BUS SELECTION (YOUR ADAPTER MAY OVERRIDE THIS)
        if config and config.i2c_bus is not None:
            self.i2c_bus_number = config.i2c_bus

        # Address from config (if overridden)
        if config and config.i2c_address:
            self.i2c_addr = config.i2c_address

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
