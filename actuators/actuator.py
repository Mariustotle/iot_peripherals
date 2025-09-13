from typing import Any, List as TypingList, Optional
from peripherals.actuators.action_decorator import ActuatorAction
from peripherals.actuators.actuator_types import ActuatorType
from peripherals.peripheral import Peripheral
from peripherals.peripheral_type import PeripheralType
from peripherals.actuators.action_decorator  import ActuatorAction, derive_params_from_signature

import inspect

class Actuator(Peripheral):   
    actuator_type: ActuatorType = None
    driver_name:str = None
    status: Optional[Any] = None
    
    def __init__(self, actuator_type:ActuatorType, name:str, driver_name:str, status:Optional[Any] = None):        
        super().__init__(PeripheralType.Actuator, name)

        self.status = status
        self.actuator_type = actuator_type
        self.driver_name = driver_name
        self._actions: list[ActuatorAction] = []
        self._autowire_actions()  # <-- reflect & register

    @property
    def actions(self) -> list[ActuatorAction]:
        return list(self._actions)
    
    def _register(self, action: ActuatorAction) -> None:
        for i, a in enumerate(self._actions):
            if a.key == action.key:
                self._actions[i] = action
                break
        else:
            self._actions.append(action)    

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
            self._register(ActuatorAction(
                key=meta["key"],
                label=meta["label"],
                description=meta["description"],
                func=member,
                params=params
            ))

    @property
    def description(self) -> str:
        return self.__str__()    
    
    def __str__(self):
        current_status = ''
        if self.status is not None:
            current_status = f' with current status of [{self.status}]'

        return f'{self.name}{current_status} (Actuator: [{self.actuator_type.name}], Driver: [{self.driver_name}])'