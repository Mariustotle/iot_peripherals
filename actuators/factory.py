from typing import Any, Dict, Type

from peripherals.actuators.relay_switches.config import RelayConfig
from peripherals.actuators.relay_switches.relay_drivers import RelayDrivers
from peripherals.actuators.relay_switches.simulator import RelaySimulator
from peripherals.factory_mapping import FactoryMapping
from peripherals.peripheral_factory import PeripheralFactory
from peripherals.peripheral_type import PeripheralType

class ActuatorFactory(PeripheralFactory):

    def __init__(self):
        super().__init__(folder_path='actuators', peripheral_type=PeripheralType.Actuator)

    _config_map: Dict[Type[Any], FactoryMapping] = {
        RelayConfig:              FactoryMapping.create(RelaySimulator,          'relay_switches',              RelayDrivers),
    }

    def get_details(self, config:Any) -> 'FactoryMapping': 
        mapping = self._config_map.get(type(config))
        if not mapping:
            raise Exception(f"Unsupported actuator config type: {type(config)}")
        return mapping

