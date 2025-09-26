
from peripherals.sensors.digital_temp_sensors.config import DigitalTempConfig
from peripherals.sensors.digital_temp_sensors.driver_base import DigitalTempDriverBase
from peripherals.sensors.digital_temp_sensors.simulator import DigitalTempSimulator
from peripherals.sensors.digital_temp_sensors.digital_temp_drivers import DigitalTempDrivers
from peripherals.sensors.sensor_factory import SensorFactory

class DigitalTempFactory:

    @staticmethod
    def create(config:DigitalTempConfig, simulate:bool = False) -> 'DigitalTempDriverBase':
        return SensorFactory.create(config, 'digital_temp_sensors', DigitalTempSimulator, DigitalTempDrivers, simulate)










