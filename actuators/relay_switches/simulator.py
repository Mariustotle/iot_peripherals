
from peripherals.actuators.relay_switches.relay_driver_base import RelayDriverBase
from peripherals.contracts.on_off_status import OnOffStatus

class RelaySimulator(RelayDriverBase):

    def _set_relay_properties(self, power_status:OnOffStatus, relay_status:OnOffStatus):
        print(f'Simulate setting relay properties: Power Status = [{power_status}], Relay Status = [{relay_status}]')


