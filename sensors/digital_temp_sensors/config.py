from pydantic import BaseModel
from typing import Optional

from peripherals.contracts.pin_config import PinConfig
from peripherals.contracts.temperature_measurement import TemperatureMeasurement
from peripherals.sensors.digital_temp_sensors.digital_temp_drivers import DigitalTempDrivers


class DigitalTempConfig(BaseModel):
    name: str = None
    driver: Optional[DigitalTempDrivers] = None
    gpio_pin: Optional[PinConfig] = None
    measurement: TemperatureMeasurement = TemperatureMeasurement.Celsius