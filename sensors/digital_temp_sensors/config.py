from pydantic import BaseModel
from typing import Optional

from peripherals.contracts.pin_config import PinConfig
from peripherals.contracts.temperature_measurement import TemperatureMeasurement
from peripherals.sensors.digital_i2c_combo_sensor.digital_combo_drivers import DigitalComboDrivers


class DigitalTempConfig(BaseModel):
    name: str = None
    driver: Optional[DigitalComboDrivers] = None
    gpio_pin: Optional[PinConfig] = None
    measurement: TemperatureMeasurement = TemperatureMeasurement.Celsius