from typing import Optional

from peripherals.contracts.i2c_address import I2CAddress
from peripherals.contracts.temperature_measurement import TemperatureMeasurement
from peripherals.sensors.digital_i2c_combo_sensor.digital_combo_drivers import DigitalComboDrivers
from src.contracts.modules.i2c_base import I2CBase


class DigitalComboConfig(I2CBase):
    name: str = None
    driver: Optional[DigitalComboDrivers] = None
    measurement: Optional[TemperatureMeasurement] = TemperatureMeasurement.Celsius