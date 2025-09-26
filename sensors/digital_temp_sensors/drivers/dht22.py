


import random
from peripherals.contracts.temperature_measurement import TemperatureMeasurement
from peripherals.sensors.digital_temp_sensors.driver_base import DigitalTempDriverBase
import Adafruit_DHT
from peripherals.sensors.digital_temp_sensors.response import DigitalTempResponse

class DHT22(DigitalTempDriverBase):
    sensor = None

    def initialize(self) -> bool:

        try:
            self.sensor = Adafruit_DHT.DHT22
            return True

        except Exception as ex:
            print(f"Oops! {ex.__class__} Unable to intialize [{self.driver_name}]. Details: {ex}")

        return False


    def _default_reading(self) -> float:        
        (humidity, temperature) = Adafruit_DHT.read_retry(self.sensor, self.gpio_pin)

        return DigitalTempResponse.create(temperature=temperature, measurement=self.config.measurement, humidity=humidity)

