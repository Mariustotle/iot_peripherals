

from ast import List
from typing import Optional

from pydantic import BaseModel
from peripherals.contracts.pins.pin_details import PinNumber
from peripherals.contracts.pins.pin_types import PinType


class DeviceFeature(BaseModel):
    name:str = None
    supported:bool = None
    enabled:bool = None

    def __init__(self):
        self.pin_configurations = []

    @staticmethod
    def create(name:str, supported:bool, enabled:bool):
        return DeviceFeature(name=name, supported=supported, enabled=enabled)
    
    def __repr__(self):
        return f"{self.name}(supported={self.supported}, enabled={self.enabled})"