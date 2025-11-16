

from typing import Any, Dict, Optional
from pydantic import BaseModel

from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_position import PinPosition

class FactoryMapping(BaseModel):
    simulator_class: Any = None
    peripheral_path:str = None
    driver_enum: Optional[Any] = None
    pins: Optional[Dict[PinPosition, PinDetails]] = None

    @staticmethod
    def create(simulator_class: Any, peripheral_path:str, driver_enum: Optional[Any] = None, pins:Optional[Dict[PinPosition, PinDetails]] = None) -> 'FactoryMapping':
        return FactoryMapping(simulator_class=simulator_class, peripheral_path=peripheral_path, driver_enum=driver_enum, pins=pins)

