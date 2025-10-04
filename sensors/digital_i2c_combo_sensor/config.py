from pydantic import BaseModel
from typing import Optional

from peripherals.contracts.i2c_address import I2CAddress
from peripherals.contracts.temperature_measurement import TemperatureMeasurement
from peripherals.sensors.digital_i2c_combo_sensor.digital_combo_drivers import DigitalComboDrivers


class DigitalComboConfig(BaseModel):
    name: str = None
    driver: Optional[DigitalComboDrivers] = None
    i2c_address: Optional[I2CAddress] = I2CAddress.Unknown
    measurement: Optional[TemperatureMeasurement] = TemperatureMeasurement.Celsius