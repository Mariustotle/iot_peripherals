from typing import Any, Dict, Optional
from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.contracts.pins.pin_types import PinType
from peripherals.contracts.temperature_measurement import TemperatureMeasurement
from peripherals.sensors.temperature_sensors.config.digital_i2c_config import DigitalI2CTemperatureConfig
from peripherals.sensors.temperature_sensors.driver_base import TemperatureDriverBase
from peripherals.sensors.temperature_sensors.response import DigitalTempResponse


class AHT10(TemperatureDriverBase):
    gpio_sd_pin: Optional[int] = None
    gpio_scl_pin: Optional[int] = None      

    def _initialize(self, name:str, config:Optional[DigitalI2CTemperatureConfig] = None) -> bool:
        self.gpio_sd_pin = config.gpio_pin_sda if config and config.gpio_pin_sda else None
        self.gpio_scl_pin = config.gpio_pin_scl if config and config.gpio_pin_scl else None

        return True
  
    
    def read_raw(self):
        humidity = 50.0
        temperature = 22.0

        # TODO: Add driver logic here
        return temperature, humidity


    def _default_reading(self) -> float:

        (temperature, humidity) = self.read_raw()

        if temperature is not None:
            if self.config.measurement == TemperatureMeasurement.Fahrenheit:
                temperature = (temperature * 9/5) + 32

        return DigitalTempResponse.create(
            temperature=temperature,
            measurement=self.config.measurement,
            humidity=humidity
        )    


    def cleanup(self):
        pass
