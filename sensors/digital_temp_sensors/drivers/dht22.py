from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.contracts.pins.pin_types import PinType
from peripherals.contracts.temperature_measurement import TemperatureMeasurement
from peripherals.sensors.digital_temp_sensors.driver_base import DigitalTempDriverBase
from peripherals.sensors.digital_temp_sensors.response import DigitalTempResponse

import Adafruit_DHT
import time

class DHT22(DigitalTempDriverBase):
    dht_device = None

    def initialize(self) -> bool:
        try:
            # TODO currently expecting a BCM mapping from the config need to allow for board as well
            self.sensor = Adafruit_DHT.DHT22
            return True

        except Exception as ex:
            print(f"Oops! {ex.__class__.__name__} - Unable to initialize [{self.driver_name}]. Details: {ex}")
            return False


    def _default_reading(self) -> DigitalTempResponse:
        if not self.dht_device:
            raise RuntimeError("DHT22 not initialized. Call initialize() first.")

        try:

            # Give the sensor a small delay before reading (helps stability)
            time.sleep(0.5)
            (humidity, temperature) = Adafruit_DHT.read_retry(self.sensor, self.gpio_pin)

            # Convert temperature if needed
            if temperature is not None and self.config.measurement == TemperatureMeasurement.Fahrenheit:
                temperature = (temperature * 9/5) + 32

            return DigitalTempResponse.create(
                temperature=temperature,
                measurement=self.config.measurement,
                humidity=humidity
            )

        except RuntimeError as ex:
            # The DHT sensors occasionally time out — just return None gracefully
            print(f"DHT22 read error: {ex}")
            return DigitalTempResponse.create(
                temperature=None,
                measurement=self.config.measurement,
                humidity=None
            )

        except Exception as ex:
            print(f"Unexpected error reading DHT22: {ex}")
            return DigitalTempResponse.create(
                temperature=None,
                measurement=self.config.measurement,
                humidity=None
            )


    def configure_available_pins(self):
        
        self.add_pin(
            pin_position=PinPosition.create(horizontal_pos=1),
            pin_details=PinDetails.create(type=PinType.Power3V, name="+")            
        )
        self.add_pin(
            pin_position=PinPosition.create(horizontal_pos=2),
            pin_details=PinDetails.create(type=PinType.DIGITAL, name="OUT", description="Digital Data Output")            
        )
        self.add_pin(
            pin_position=PinPosition.create(horizontal_pos=3),
            pin_details=PinDetails.create(type=PinType.Ground, name="-")            
        )