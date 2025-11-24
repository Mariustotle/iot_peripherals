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
    AHT10/AHT20 Temperature + Humidity Sensor (High Precision I2C)
    Datasheet formulas implemented:
        - Humidity:     RH = (S_rh / 2^20) * 100
        - Temperature:  T = ((S_t / 2^20) * 200) - 50
    """
    DEFAULT_I2C_ADDR:int = 0x38
    DEFAULT_BUS_NUMBER:int = 1

    i2c_addr:int = None
    i2c_bus_number:int = None
    bus: Optional[smbus2.SMBus] = None    


    def __init__(self, config:DigitalI2CTemperatureConfig, simulated:bool = False, pins:Optional[Dict[PinPosition, PinDetails]] = None):
        super().__init__(config, simulated, pins)
        self.bus: Optional[smbus2.SMBus] = None
        self.i2c_addr = config.i2c_address.value if config.i2c_address and config.i2c_address != 0 else self.DEFAULT_I2C_ADDR
        self.i2c_bus_number = config.channel if config.channel else self.DEFAULT_BUS_NUMBER      
        self.initialized = False


    def _initialize(self, name: str, config: Optional[DigitalI2CTemperatureConfig] = None) -> bool:

        debug = []

        debug.append(f"Initializing AHT10/AHT20 sensor '{name}'")
        debug.append(f"  • I2C Bus Number : {self.i2c_bus_number}")
        debug.append(f"  • I2C Address    : 0x{self.i2c_addr:02X} ({self.i2c_addr})")

        # Check if bus device exists (/dev/i2c-X)
        import os
        bus_path = f"/dev/i2c-{self.i2c_bus_number}"
        if not os.path.exists(bus_path):
            raise RuntimeError(
                "\n".join(debug + [
                    f"  ✖ ERROR: I2C bus device '{bus_path}' does NOT exist.",
                    "  → I2C not enabled, wrong bus number, or dtoverlay disabled.",
                ])
            )

        # Try opening bus
        try:
            self.bus = smbus2.SMBus(self.i2c_bus_number)
            debug.append("  ✔ Opened I2C bus successfully")
        except Exception as ex:
            raise RuntimeError(
                "\n".join(debug + [
                    "  ✖ ERROR: Failed to open I2C bus.",
                    f"  System error: {ex}",
                ])
            )

        # Try soft reset (AHT10 only)
        try:
            self.bus.write_byte_data(self.i2c_addr, 0xBA, 0x00)
            sleep(0.02)
            debug.append("  ✔ Soft reset ACK (likely AHT10)")
        except Exception as ex:
            debug.append(f"  • Soft reset ignored (likely AHT20). Details: {ex}")

        # Initialization (AHT10 = 0xE1, AHT20 = 0xBE)
        try:
            self.bus.write_i2c_block_data(self.i2c_addr, 0xBE, [0x08, 0x00])
            sleep(0.01)
            debug.append("  ✔ Initialization command 0xBE succeeded")
        except Exception as ex:
            raise RuntimeError(
                "\n".join(debug + [
                    "  ✖ ERROR: Initialization command failed.",
                    f"  Low-level SMBus error: {ex}",
                    "",
                    "Possible causes:",
                    "  • Device not connected",
                    "  • Wrong SDA/SCL pins",
                    "  • Wrong I2C bus (0 vs 1)",
                    "  • No pull-up resistors",
                    "  • AHT sensor not powered",
                    "  • Cheap module is actually AHT20 (OK) but not responding",
                ])
            )

        self.initialized = True
        return True


    def read_raw(self):

        if not self.initialized:
            raise RuntimeError("AHT10: read_raw() called before initialization")

        try:
            self.bus.write_i2c_block_data(self.i2c_addr, 0xAC, [0x33, 0x00])
        except Exception as ex:
            raise RuntimeError(f"AHT10: Failed to trigger measurement: {ex}")

        sleep(0.1)

        try:
            data = self.bus.read_i2c_block_data(self.i2c_addr, 0x00, 6)
        except Exception as ex:
            raise RuntimeError(f"AHT10: Failed to read data: {ex}")

        raw_humidity = ((data[1] << 12) |
                        (data[2] << 4) |
                        (data[3] >> 4))

        raw_temp = (((data[3] & 0x0F) << 16) |
                    (data[4] << 8) |
                    data[5])

        humidity = (raw_humidity / 1048576.0) * 100.0
        temperature = ((raw_temp / 1048576.0) * 200.0) - 50.0

        return temperature, humidity


    def _default_reading(self):

        temperature, humidity = self.read_raw()

        if temperature is not None and self.config.measurement == TemperatureMeasurement.Fahrenheit:
            temperature = (temperature * 9/5) + 32

        return DigitalTempResponse.create(
            temperature=temperature,
            measurement=self.config.measurement,
            humidity=humidity,
            decimal_places=self.config.number_of_decimal_places
        )


    def cleanup(self):
        if self.bus:
            try:
                self.bus.close()
            except:
                pass
            self.bus = None
