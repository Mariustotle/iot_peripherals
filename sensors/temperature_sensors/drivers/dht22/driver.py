from typing import Any, Dict, Optional
from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.contracts.pins.pin_types import PinType
from peripherals.contracts.temperature_measurement import TemperatureMeasurement
from peripherals.devices.device_base import DeviceBase
from peripherals.sensors.temperature_sensors.config.digital_config import DigitalTemperatureConfig
from peripherals.sensors.temperature_sensors.driver_base import TemperatureDriverBase
from peripherals.sensors.temperature_sensors.response import DigitalTempResponse

import Adafruit_DHT
import time

class DHT22(TemperatureDriverBase):
    dht_device = None
    gpio_pin = None

    def __init__(self, config:DigitalTemperatureConfig, device:DeviceBase, simulated:bool = False, pins:Optional[Dict[PinPosition, PinDetails]] = None):
        super().__init__(config, device, simulated, pins)

    def _initialize(self, name:str, config:Optional[DigitalTemperatureConfig] = None) -> bool:
        self.gpio_pin = config.gpio_pin.pin_number if config and config.gpio_pin else None

        # TODO currently expecting a BCM mapping from the config need to allow for board as well
        self.dht_device = Adafruit_DHT.DHT22
        return True


    def _default_reading(self) -> DigitalTempResponse:
        if not self.dht_device:
            raise RuntimeError("DHT22 not initialized. Call initialize() first.")

        try:

            # Give the sensor a small delay before reading (helps stability)
            time.sleep(0.5)
            (humidity, temperature) = Adafruit_DHT.read_retry(self.dht_device, self.gpio_pin)

            # Debug info
            print(f"DHT22 Raw Readings - Temp: {temperature}, Humidity: {humidity}")
            time.sleep(5)

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
        
