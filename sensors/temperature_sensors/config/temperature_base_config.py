

from typing import Optional

from pydantic import BaseModel
from peripherals.contracts.temperature_measurement import TemperatureMeasurement
from peripherals.sensors.temperature_sensors.temperature_drivers import TemperatureDrivers

class TemperatureBaseConfig(BaseModel):
    name: str = None
    driver: Optional[TemperatureDrivers] = None
    measurement: TemperatureMeasurement = TemperatureMeasurement.Celsius