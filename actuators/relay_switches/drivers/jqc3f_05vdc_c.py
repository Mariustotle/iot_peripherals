
from typing import Literal
import RPi.GPIO as GPIO

from peripherals.actuators.relay_switches.relay_config import RelayConfig
from peripherals.actuators.relay_switches.relay_driver_base import RelayDriverBase
from peripherals.contracts.gpio_status import GPIOStatus
from peripherals.contracts.on_off_status import OnOffStatus

class JQC3F_05VDC_C(RelayDriverBase):
    board_type:str = None
    gpio_level:GPIOStatus = None

    @property
    def gpio_status(self) -> Literal[0]:
        return GPIO.LOW if self.gpio_level == GPIOStatus.Low else GPIO.HIGH

    def __get_gpio_level(self, relay_status:OnOffStatus) -> 'GPIOStatus':
        if relay_status == OnOffStatus.On:
            return GPIOStatus.Low if self.config.is_low_voltage_trigger else GPIOStatus.High
        else:
            return GPIOStatus.High if self.config.is_low_voltage_trigger else GPIOStatus.Low        
       
    def __init__(self, config:RelayConfig, simulated = False):
        super().__init__(config, simulated) 

    def _switch_relay_on(self):
        self.gpio_level = self.__get_gpio_level(OnOffStatus.On)        
        GPIO.output(self.relay_pin, self.gpio_status)

    def _switch_relay_off(self):
        self.gpio_level = self.__get_gpio_level(OnOffStatus.Off) 
        GPIO.output(self.relay_pin, self.gpio_status)

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
        
        self.gpio_level = self.__get_gpio_level(OnOffStatus.Off)
        GPIO.setup(self.relay_pin, GPIO.OUT, initial=self.gpio_status)
        print(f'Initialized >> {self}')

    def cleanup(self):
        GPIO.cleanup()

    def __str__(self):
        return f'{super().__str__()} | Board Type = [{self.board_type}] | GPIO Pin = [{self.relay_pin}] | GPIO Level = [{self.gpio_level}]' 
