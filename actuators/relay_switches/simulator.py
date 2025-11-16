from typing import Optional, Dict
from peripherals.actuators.relay_switches.config import RelayConfig
from peripherals.actuators.relay_switches.driver_base import RelayDriverBase
from peripherals.contracts.on_off_status import OnOffStatus
from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_position import PinPosition

class RelaySimulator(RelayDriverBase):

    def __init__(self, config:RelayConfig, pins:Optional[Dict[PinPosition, PinDetails]] = None):
        super().__init__(config, False, pins)

    def _set_relay_properties(self, relay_status:OnOffStatus):
        print(f'Simulate setting relay properties: Relay Status = [{relay_status}]')
