
from typing import Optional

from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.contracts.pins.pin_types import PinType
from peripherals.devices.device_feature import DeviceFeature

class GpioPinDetails(PinDetails):
    special_mode:Optional[PinType] = None
    feature:Optional[DeviceFeature] = None
    board_pin:int = None
    gpio_pin:Optional[int] = None

    @property
    def standard_mode(self) -> PinType:
        return self.type

    @staticmethod
    def create(board_pin:int, standard_mode:PinType, gpio_pin:Optional[int] = None, label:Optional[str] = None, source_pin:Optional[PinPosition] = None, special_mode:Optional[PinType] = None, feature:Optional[DeviceFeature] = None):
        return GpioPinDetails(board_pin=board_pin, gpio_pin=gpio_pin, type=standard_mode, label=label, source_pin=source_pin, special_mode=special_mode, feature=feature)


