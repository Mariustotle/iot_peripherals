from pydantic import BaseModel
from typing import Optional

from peripherals.contracts.temperature_measurement import TemperatureMeasurement
from peripherals.sensors.digital_temp_sensors.temperature_drivers import DigitalTempDrivers


class DigitalTempConfig(BaseModel):
    name: str = None
    driver: Optional[DigitalTempDrivers] = None
    gpio_pin: Optional[int] = None
    measurement: TemperatureMeasurement = TemperatureMeasurement.Celsius