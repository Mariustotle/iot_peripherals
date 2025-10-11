from threading import RLock
from typing import Any, List, Optional

from peripherals.actuators.actuator import Actuator
from peripherals.actuators.factory import ActuatorFactory
from peripherals.communication.communication import Communication
from peripherals.communication.factory import CommunicationFactory
from peripherals.catalog.catalog_category import CatalogCategory
from peripherals.sensors.sensor import Sensor
from peripherals.sensors.factory import SensorFactory

class DeviceCatalog:

    _lock:RLock = None

    sensors:CatalogCategory[Sensor] = None
    actuators:CatalogCategory[Actuator] = None
    communication_modules:CatalogCategory[Communication] = None

    @property
    def peripherals(self) -> List[Any]:
        with self._lock:
            return self.sensors.all + self.actuators.all + self.communication_modules.all

    def register_sensors(self, sensors_config:List[Any], is_simulated:bool) -> None:
        factory = SensorFactory()
        for config in sensors_config:
            sensor = factory.create(config, simulate=is_simulated)
            self.sensors.register(sensor)

    def register_actuators(self, actuators_config:List[Any], is_simulated:bool) -> None:
        factory = ActuatorFactory()
        for config in actuators_config:
            actuator = factory.create(config, simulate=is_simulated)
            self.actuators.register(actuator)

    def register_communication_modules(self, communications_config:List[Any], is_simulated:bool) -> None:
        factory = CommunicationFactory()
        for config in communications_config:
            module = factory.create(config, simulate=is_simulated)
            self.communication_modules.register(module)

    def __init__(self,
            is_simulated:bool = False,           
            sensors_config:Optional[List[Any]] = None,
            actuators_config:Optional[List[Any]] = None,                 
            communications_config:Optional[List[Any]] = None   
        ):
    
        self._lock = RLock()
        self.sensors = CatalogCategory[Sensor]()
        self.actuators = CatalogCategory[Actuator]()
        self.communication_modules = CatalogCategory[Communication]()

        if sensors_config is not None:
            self.register_sensors(sensors_config, is_simulated)

        if actuators_config is not None:
            self.register_actuators(actuators_config, is_simulated)

        if communications_config is not None:
            self.register_communication_modules(communications_config, is_simulated)
        
