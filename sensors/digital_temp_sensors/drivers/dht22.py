from peripherals.contracts.temperature_measurement import TemperatureMeasurement
from peripherals.sensors.digital_temp_sensors.driver_base import DigitalTempDriverBase
from peripherals.sensors.digital_temp_sensors.response import DigitalTempResponse

import os
import Adafruit_DHT


class DHT22(DigitalTempDriverBase):
    sensor = None

    def initialize(self) -> bool:
        try:
            # Force the Adafruit library to treat this as a Raspberry Pi environment
            os.environ.setdefault("ADAFRUIT_DHT_FORCE_RPI", "1")

            # Initialize sensor type
            self.sensor = Adafruit_DHT.DHT22
            return True

        except Exception as ex:
            print(f"Oops! {ex.__class__.__name__} - Unable to initialize [{self.driver_name}]. Details: {ex}")
            return False


    def _default_reading(self) -> DigitalTempResponse:
        # Perform a retry-based read (handles transient GPIO timing issues)
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.gpio_pin)

        # Convert temperature if needed
        if temperature is not None and self.config.measurement == TemperatureMeasurement.Fahrenheit:
            temperature = (temperature * 9/5) + 32

        # Package the result into your domain response object
        return DigitalTempResponse.create(
            temperature=temperature,
            measurement=self.config.measurement,
            humidity=humidity
        )
