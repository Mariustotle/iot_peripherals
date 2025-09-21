
from typing import Literal
import RPi.GPIO as GPIO

from peripherals.actuators.relay_switches.relay_config import RelayConfig
from peripherals.actuators.relay_switches.relay_driver_base import RelayDriverBase
from peripherals.contracts.on_off_status import OnOffStatus

class JQC3F_05VDC_C(RelayDriverBase):
    board_type:str = None

    def __gpio_value(self, relay_status:OnOffStatus) -> Literal[0]:
        if relay_status == OnOffStatus.On:
            return GPIO.LOW if self.config.is_low_voltage_trigger else GPIO.HIGH
        else:
            return GPIO.HIGH if self.config.is_low_voltage_trigger else GPIO.LOW

    def __init__(self, config:RelayConfig, simulated = False):
        super().__init__(config, simulated) 

    def _switch_relay_on(self):
        GPIO.output(self.relay_pin, self.__gpio_value(OnOffStatus.On))

    def _switch_relay_off(self):        
        GPIO.output(self.relay_pin, self.__gpio_value(OnOffStatus.Off))

    def initialize(self) -> str:

        if (self.config.gpio_pin is not None):
            GPIO.setmode(GPIO.BCM)   # BCM pin numbering
            self.board_type = 'BCM'
            self.relay_pin = self.config.gpio_pin

        elif (self.config.pin_position is not None):
            GPIO.setmode(GPIO.BOARD) # BOARD pin numbering
            self.board_type = 'BOARD'
            self.relay_pin = self.config.pin_position

        else:
            raise Exception("Pin configurtation incorrect, please set either gpio_pin (GPIO Numbering) or pin_position (PIN position numbering).")

        GPIO.setup(self.relay_pin, GPIO.OUT, initial=self.__gpio_value(OnOffStatus.Off))
        print(f'Initialized >> {self}')

    def cleanup(self):
        GPIO.cleanup()

    def __str__(self):
        return f'{super().__str__()} | Board Type = [{self.board_type}] | GPIO Pin = [{self.relay_pin}]' 
