

from typing import Any, Optional
from pydantic import BaseModel

class FactoryMapping(BaseModel):
    simulator_class: Any = None
    peripheral_path:str = None
    driver_enum: Optional[Any] = None

    @staticmethod
    def create(simulator_class: Any, peripheral_path:str, driver_enum: Optional[Any] = None) -> 'FactoryMapping':
        return FactoryMapping(simulator_class=simulator_class, peripheral_path=peripheral_path, driver_enum=driver_enum)

