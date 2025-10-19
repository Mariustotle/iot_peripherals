
from typing import Optional

from peripherals.contracts.pins.pin_types import PinType
from peripherals.devices.device_feature import DeviceFeature

class PinDetails:
    standard_mode:PinType = None
    special_mode:Optional[PinType] = None
    feature:Optional[DeviceFeature] = None    

    def __init__(self, standard_mode:PinType, special_mode:Optional[PinType] = None, feature:Optional[DeviceFeature] = None):
        self.standard_mode = standard_mode
        self.special_mode = special_mode
        self.feature = feature
