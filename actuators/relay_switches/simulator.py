
from peripherals.actuators.relay_switches.relay_driver_base import RelayDriverBase

class RelaySimulator(RelayDriverBase):

    def _switch_relay_on(self):
        print('Simulate switching relay ON...')

    def _switch_relay_off(self):
        print('Simulate switching relay OFF...')


