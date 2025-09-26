
from peripherals.actuators.relay_switches.driver_base import RelayDriverBase
from peripherals.contracts.on_off_status import OnOffStatus

class RelaySimulator(RelayDriverBase):

    def _set_relay_properties(self, relay_status:OnOffStatus):
        print(f'Simulate setting relay properties: Relay Status = [{relay_status}]')


