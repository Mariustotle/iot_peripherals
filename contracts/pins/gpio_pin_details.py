
from typing import Optional

from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_types import PinType
from peripherals.devices.device_feature import DeviceFeature

class GpioPinDetails(PinDetails):
    special_mode:Optional[PinType] = None
    feature:Optional[DeviceFeature] = None
    board_pin:int = None
    gpio_pin:Optional[int] = None

    @property
    def active_pin_type(self):
        return self.special_mode if self.multi_function and self.feature and self.feature.enabled else self.standard_mode

    @property
    def inactive_pin_type(self):
        if self.special_mode is None:
            return None        
        return self.standard_mode if self.multi_function and self.feature and self.feature.enabled else self.special_mode

    @property
    def standard_mode(self) -> PinType:
        return self.type

    @property
    def multi_function(self):
        return self.special_mode is not None

    @property
    def label(self):
        is_special = self.multi_function and self.feature and self.feature.enabled
        gpio = '' if not self.gpio_pin or is_special else f'-G{self.gpio_pin}'
        
        return f'{self.active_pin_type.short }{gpio}'
    
    def __str__(self):
        is_special = self.multi_function and self.feature and self.feature.enabled
        alternate_pin = self.type if is_special else self.special_mode
        
        type_detail = f'Type: {self.type.name} [{self.type.short}]' if not self.special_mode else f'Active type: {self.active_pin_type.name} [{self.active_pin_type.short}], Alternative type: [{alternate_pin.name}]'

        feature = f', Feature: {self.feature.name} (Enabled={self.feature.enabled})' if self.feature else ''
        descript = f', Description: {self.description}' if self.description else ''

        return f'{self.label} ({'In Use' if self.in_use else 'Available'}) >> {type_detail}{feature}{descript}'

    @staticmethod
    def create(board_pin:int, standard_mode:PinType, gpio_pin:Optional[int] = None, name:Optional[str] = None, special_mode:Optional[PinType] = None, feature:Optional[DeviceFeature] = None, in_use:bool = False, description:Optional[str] = None):

        if special_mode is not None and description is None:
            description = f'DUAL Mode PIN - Standard: {standard_mode.name} [{standard_mode.short}], Special: {special_mode.name} [{special_mode.short}]'

        return GpioPinDetails(board_pin=board_pin, gpio_pin=gpio_pin, type=standard_mode, name=name, special_mode=special_mode, feature=feature, in_use=in_use, description=description)


