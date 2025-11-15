from peripherals.sensors.temperature_sensors.config.temperature_base_config import TemperatureBaseConfig
from src.contracts.modules.i2c_base import I2CBase

class DigitalI2CTemperatureConfig(I2CBase, TemperatureBaseConfig):
    pass
