
from peripherals.actuators.relay_switches.driver_base import RelayDriverBase
from peripherals.contracts.on_off_status import OnOffStatus
from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.contracts.pins.pin_types import PinType

class RelaySimulator(RelayDriverBase):

    def _set_relay_properties(self, relay_status:OnOffStatus):
        print(f'Simulate setting relay properties: Relay Status = [{relay_status}]')


    def configure_available_pins(self):
        
        self.add_pin(
            pin_position=PinPosition.create(horizontal_pos=1),
            pin_details=PinDetails.create(type=PinType.Ground, label='G')            
        )
        self.add_pin(
            pin_position=PinPosition.create(horizontal_pos=2),
            pin_details=PinDetails.create(type=PinType.DIGITAL, label='D')            
        )
        self.add_pin(
            pin_position=PinPosition.create(horizontal_pos=3),
            pin_details=PinDetails.create(type=PinType.Power3V, label='V')            
        )