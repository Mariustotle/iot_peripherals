
import RPi.GPIO as GPIO
import time

from peripherals.actuators.relay_switches.relay_driver_base import RelayDriverBase
from peripherals.actuators.relay_switches.relay_status import RelayStatus

class JQC3F_05VDC_C(RelayDriverBase):

    def __init__(self, config, simulated = False):
        super().__init__(config, simulated)

        default_state = GPIO.HIGH if config.default_status == RelayStatus.OFF else GPIO.LOW

        GPIO.setmode(GPIO.BCM)   # BCM pin numbering
        GPIO.setup(self.relay_pin, GPIO.OUT, initial=default_state)

    def _switch_on(self):
        print('[JQC3F_05VDC_C] switching relay ON')
        GPIO.output(self.relay_pin, GPIO.HIGH)

    def _switch_off(self):        
        print('[JQC3F_05VDC_C] switching relay OFF')
        GPIO.output(self.relay_pin, GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup()


