
from abc import abstractmethod
from peripherals.sensors.read_decorator  import ReadAction, derive_params_from_signature
from peripherals.peripheral import Peripheral
from peripherals.peripheral_type import PeripheralType
from peripherals.sensors.sensor_reading import SensorReading
from peripherals.sensors.sensor_type import SensorType
from peripherals.sensors.unit_type import UnitType
from typing import TypeVar

import inspect

T = TypeVar('T')

class Sensor(Peripheral):
    sensor_type: SensorType = None
    unit_type: UnitType = None
    driver_name:str = None
    
    def __init__(self, sensor_type:SensorType, name:str, driver_name:str, unit_type:UnitType = UnitType.Unkown):        
        super().__init__(PeripheralType.Sensor, name)

        self.sensor_type = sensor_type
        self.driver_name = driver_name
        self.unit_type = unit_type
        self._reads: list[ReadAction] = []

    @property
    def reading_options(self) -> list[ReadAction]:
        return list(self._reads)
    
    def _register(self, action: ReadAction) -> None:
        for i, a in enumerate(self._reads):
            if a.key == action.key:
                self._reads[i] = action
                break
        else:
            self._reads.append(action)    

    def _autowire_actions(self) -> None:
        # find bound methods with @action
        for _, member in inspect.getmembers(self, predicate=inspect.ismethod):
            meta = getattr(member, "_menu_action_meta", None)
            is_action = getattr(member, "_is_menu_action", False)
            if not is_action or meta is None:
                continue

            params = meta["params"]
            if params is None:
                params = derive_params_from_signature(member)
            self._register(ReadAction(
                key=meta["key"],
                label=meta["label"],
                description=meta["description"],
                func=member,
                params=params
            ))

    @abstractmethod
    async def default_read(self) -> SensorReading[T]: pass

    def get_description(self) -> str:
        return f'{self.name}. Sensor: [{self.sensor_type.name}], Driver: [{self.driver_name}]'

    def __str__(self):
        return f'{self.name}. Sensor: [{self.sensor_type.name}], Driver: [{self.driver_name}]. Override "__str__(self)" in derived class to include current status.'