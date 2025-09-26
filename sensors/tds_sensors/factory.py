
from peripherals.sensors.sensor_factory import SensorFactory
from peripherals.sensors.tds_sensors.tds_drivers import TDSDrivers
from peripherals.sensors.tds_sensors.config import TDSConfig
from peripherals.sensors.tds_sensors.driver_base import TDSDriverBase
from peripherals.sensors.tds_sensors.simulator import TDSSimulator

class TDSFactory:

    @staticmethod
    def create(config:TDSConfig, simulate:bool = False) -> 'TDSDriverBase':
        return SensorFactory.create(config, 'tds_sensors', TDSSimulator, TDSDrivers, simulate)









