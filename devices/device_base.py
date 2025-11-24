from typing import List, cast, Dict, Optional

from peripherals.contracts.board.board_base import BoardBase
from peripherals.contracts.device_type import DeviceType
from peripherals.contracts.pins.gpio_pin_details import GpioPinDetails
from peripherals.contracts.pins.pin_config import PinConfig
from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_numbering_scheme import PinNumberingScheme
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.contracts.pins.pin_types import PinType
from peripherals.devices.adapters.adapter_base import AdapterBase

class DeviceBase(BoardBase):
    device_type:DeviceType = None
    adapter:AdapterBase = None

    @property
    def device_pins(self) -> Dict[PinPosition, GpioPinDetails]:
        return cast(Dict[PinPosition, GpioPinDetails], self.pins)           
    
    def __init__(self, device_type:DeviceType, adapter:AdapterBase, default_pin_type:PinType):
        self.device_type = device_type
        self.adapter = adapter        
        name = device_type.name

        super().__init__(name=name, default_pin_type=default_pin_type, default_use_state=False)

    def _configure_pins(self, pins:Optional[Dict[PinPosition, PinDetails]] = None):        
        # configured_pins will not be used in this context
        pin_layout = self.get_pin_layout(adapter=self.adapter)

        for position, details in pin_layout.items():
            self.add_gpio_pin(pin_position=position, pin_details=details)

    def add_gpio_pin(self, pin_details:GpioPinDetails, pin_position:PinPosition):
        super().add_pin(pin_details=pin_details, pin_position=pin_position)

    def get_gpio_pin(self, pin: int, scheme: PinNumberingScheme) -> tuple[PinPosition, GpioPinDetails] | tuple[None, None]:
        # Ensure you're iterating over .items(), not the function itself
        found_key = next(
            (
                k
                for k, v in self.device_pins.items()
                if (
                    (scheme == PinNumberingScheme.BCM and getattr(v, "gpio_pin", None) == pin)
                    or (scheme == PinNumberingScheme.BOARD and getattr(v, "board_pin", None) == pin)
                )
            ),
            None
        )

        return (None, None) if not found_key else (found_key, self.device_pins[found_key])


    def validate_i2c_pins(
                self,
                name: str,
                channel: int,
                i2c_address: int,
                sda_config: PinConfig,
                scl_config: PinConfig
            ) -> bool:
        
        return True