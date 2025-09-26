from pydantic import BaseModel
from typing import Optional

from peripherals.contracts.temperature_measurement import TemperatureMeasurement
from peripherals.sensors.temperature_switch.temp_switch_drivers import TempSwitchDrivers


class TempSwitchConfig(BaseModel):
    name: str = None
    driver: Optional[TempSwitchDrivers] = None
    adc_module:str = None
    gpio_out_pin: Optional[int] = None
    switch_threshold:Optional[float] = None     # e.g. ">10"
    measurement: TemperatureMeasurement = TemperatureMeasurement.Celsius