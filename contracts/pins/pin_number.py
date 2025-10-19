
from typing import Optional

from peripherals.devices.device_feature import DeviceFeature

class PinNumber:
    gpio_pin:Optional[int] = None
    board_pin:Optional[int] = None

    def __init__(self, gpio_pin:Optional[int] = None, board_pin:Optional[int] = None):
        self.gpio_pin = gpio_pin
        self.board_pin = board_pin
