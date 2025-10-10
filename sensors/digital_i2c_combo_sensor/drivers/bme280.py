import board
import busio

from Adafruit-BME280 import Adafruit_BME280_I2C
from peripherals.contracts.i2c_address import I2CAddress
from peripherals.contracts.temperature_measurement import TemperatureMeasurement
from peripherals.sensors.digital_i2c_combo_sensor.driver_base import DigitalComboDriverBase
from peripherals.sensors.digital_i2c_combo_sensor.response import DigitalComboResponse

class BME280(DigitalComboDriverBase):

    def initialize(self) -> bool:

        try:
            # Set up I²C bus
            self.i2c = busio.I2C(board.SCL, board.SDA)

            # Create sensor instance at default I2C address 0x76 (sometimes 0x77)
            address = 0x76 if self.config.i2c_address == I2CAddress.X76 else 0x77

            self.sensor = Adafruit_BME280_I2C(self.i2c, address=address)

            # Optional: tweak settings
            self.sensor.sea_level_pressure = 1013.25  # for altitude compensation
            return True

        except Exception as ex:
            print(f"Oops! {ex.__class__} Unable to intialize [{self.driver_name}]. Details: {ex}")

        return False
    
    def _read_raw(self):
        if not self.sensor:
            raise RuntimeError("BME280 not initialized")

        # Direct readings
        temperature_c = self.sensor.temperature
        pressure_hpa = self.sensor.pressure
        humidity_pct = self.sensor.humidity

        return (temperature_c, pressure_hpa, humidity_pct)


    def _default_reading(self) -> float:
        (temperature, air_pressure, hygrometer) = self._read_raw(self.gpio_pin)

        if temperature is not None:
            if self.config.measurement == TemperatureMeasurement.Fahrenheit:
                temperature = (temperature * 9/5) + 32

        return DigitalComboResponse.create(
            temperature=temperature,
            measurement=self.config.measurement,
            air_pressure=air_pressure,
            hygrometer=hygrometer
        )
