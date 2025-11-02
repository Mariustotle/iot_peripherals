
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

    @property
    def multi_function(self):
        return self.special_mode is not None

    @property
    def label(self):
        is_special = self.multi_function and self.feature and self.feature.enabled

        label = self.standard_mode.short if (not self.multi_function or not is_special) else self.special_mode.short            
        gpio = '' if not self.gpio_pin or is_special else f'-G{self.gpio_pin}'
        
        return f'{label}{gpio}'


    @staticmethod
    def create(board_pin:int, standard_mode:PinType, gpio_pin:Optional[int] = None, name:Optional[str] = None, special_mode:Optional[PinType] = None, feature:Optional[DeviceFeature] = None, in_use:bool = False):
        return GpioPinDetails(board_pin=board_pin, gpio_pin=gpio_pin, type=standard_mode, name=name, special_mode=special_mode, feature=feature, in_use=in_use)


