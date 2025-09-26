
from peripherals.sensors.sensor_factory import SensorFactory
from peripherals.sensors.temperature_switch.config import TempSwitchConfig
from peripherals.sensors.temperature_switch.driver_base import TempSwitchDriverBase
from peripherals.sensors.temperature_switch.simulator import TempSwitchSimulator
from peripherals.sensors.temperature_switch.temp_switch_drivers import TempSwitchDrivers

class TempSwitchFactory:

    @staticmethod
    def create(config:TempSwitchConfig, simulate:bool = False) -> 'TempSwitchDriverBase':
        return SensorFactory.create(config, 'temperature_switch', TempSwitchSimulator, TempSwitchDrivers, simulate)









