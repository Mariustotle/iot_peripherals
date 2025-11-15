from typing import Any, Dict, Type

from peripherals.factory_mapping import FactoryMapping
from peripherals.peripheral_factory import PeripheralFactory
from peripherals.peripheral_type import PeripheralType
from peripherals.sensors.temperature_sensors.config.analog_config import AnalogTemperatureConfig
from peripherals.sensors.temperature_sensors.config.digital_config import DigitalTemperatureConfig
from peripherals.sensors.temperature_sensors.config.digital_i2c_config import DigitalI2CTemperatureConfig
from peripherals.sensors.temperature_sensors.temperature_drivers import TemperatureDrivers
from peripherals.sensors.temperature_sensors.simulator import TemperatureSimulator
from peripherals.sensors.tds_sensors.config import TDSConfig
from peripherals.sensors.tds_sensors.simulator import TDSSimulator
from peripherals.sensors.tds_sensors.tds_drivers import TDSDrivers
from peripherals.sensors.temperature_switch.config import TempSwitchConfig
from peripherals.sensors.temperature_switch.simulator import TempSwitchSimulator
from peripherals.sensors.temperature_switch.temp_switch_drivers import TempSwitchDrivers

class SensorFactory(PeripheralFactory):

    def __init__(self):
        super().__init__(folder_path='sensors', peripheral_type=PeripheralType.Sensor)

    _config_map: Dict[Type[Any], FactoryMapping] = {
        TDSConfig:                      FactoryMapping.create(TDSSimulator,          'tds_sensors',              TDSDrivers),
        TempSwitchConfig:               FactoryMapping.create(TempSwitchSimulator,   'temperature_switch',       TempSwitchDrivers),
        AnalogTemperatureConfig:        FactoryMapping.create(TemperatureSimulator,  'temperature_sensors',      TemperatureDrivers),
        DigitalTemperatureConfig:       FactoryMapping.create(TemperatureSimulator,  'temperature_sensors',      TemperatureDrivers),
        DigitalI2CTemperatureConfig:    FactoryMapping.create(TemperatureSimulator,  'temperature_sensors',      TemperatureDrivers),

    }

    def get_details(self, config:Any) -> 'FactoryMapping': 
        mapping = self._config_map.get(type(config))
        if not mapping:
            raise Exception(f"Unsupported sensor config type: {type(config)}")
        return mapping

