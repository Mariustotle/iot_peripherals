from typing import Optional, Type, Any

from peripherals.peripheral_type import PeripheralType

class ClassMapping:
    label: str
    class_type: Optional[Type[Any]]
    peripheral_type: Optional[PeripheralType]

    def __init__(self, label: str, peripheral_type:Optional[PeripheralType] = None, class_type: Optional[Type[Any]] = None) -> None:
        self.label = label
        self.class_type = class_type
        self.peripheral_type = peripheral_type

    Undefined = ("Undefined", None, None)