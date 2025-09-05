
from peripherals.actuators.relay_switches.relay_driver_base import RelayDriverBase

class JQC3F_05VDC_C(RelayDriverBase):

    def _switch_on(self):
        print('Simulate switching relay ON')

    def _switch_off(self):
        print('Simulate switching relay OFF')


