
from peripherals.sensors.digital_i2c_combo_sensor.config import DigitalComboConfig
from peripherals.sensors.digital_i2c_combo_sensor.digital_combo_drivers import DigitalComboDrivers
from peripherals.sensors.digital_i2c_combo_sensor.driver_base import DigitalComboDriverBase
from peripherals.sensors.digital_i2c_combo_sensor.simulator import DigitalComboSimulator
from peripherals.sensors.sensor_factory import SensorFactory

class DigitalComboFactory:

    @staticmethod
    def create(config:DigitalComboConfig, simulate:bool = False) -> 'DigitalComboDriverBase':
        return SensorFactory.create(config, 'digital_temp_sensors', DigitalComboSimulator, DigitalComboDrivers, simulate)










