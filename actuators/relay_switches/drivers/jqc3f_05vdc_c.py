
from typing import Literal
import RPi.GPIO as GPIO

from peripherals.actuators.relay_switches.relay_config import RelayConfig
from peripherals.actuators.relay_switches.relay_driver_base import RelayDriverBase
from peripherals.contracts.gpio_status import GPIOStatus
from peripherals.contracts.input_output import InputOutput
from peripherals.contracts.on_off_status import OnOffStatus
from peripherals.contracts.switch_method import SwitchMethod

class JQC3F_05VDC_C(RelayDriverBase):
    board_type:str = None
    gpio_level:GPIOStatus = None
    switch_method:SwitchMethod = SwitchMethod.Level
    direction:InputOutput = InputOutput.Output

    @property
    def gpio_status(self) -> Literal[0]:
        return GPIO.LOW if self.gpio_level == GPIOStatus.Low else GPIO.HIGH
    
    @property
    def gpio_direction(self) -> Literal[0]: 
        return GPIO.OUT if self.direction == InputOutput.Output else GPIO.IN
    

    def __get_gpio_level(self, relay_status:OnOffStatus) -> 'GPIOStatus':
        if relay_status == OnOffStatus.On:
            return GPIOStatus.Low if self.config.is_low_voltage_trigger else GPIOStatus.High
        else:
            return GPIOStatus.High if self.config.is_low_voltage_trigger else GPIOStatus.Low
    
    def __get_gpio_direction(self, relay_status:OnOffStatus) -> 'InputOutput':
        if self.switch_method == SwitchMethod.Level:
            return InputOutput.Output
        elif self.power_status == OnOffStatus.On:
            return InputOutput.Output
        else:
            return InputOutput.Input

       
    def __init__(self, config:RelayConfig, simulated = False):
        super().__init__(config, simulated) 


    def _set_relay_properties(self, power_status:OnOffStatus, relay_status:OnOffStatus):

        self.gpio_level = self.__get_gpio_level(relay_status)
        GPIO.output(self.relay_pin, self.gpio_status)

        if (self.switch_method == SwitchMethod.Direction):
            self.direction = self.__get_gpio_direction(power_status)
            GPIO.setup(self.relay_pin, self.gpio_direction)
        

    def initialize(self) -> str:

        GPIO.setmode(GPIO.BCM)   # BCM pin numbering
        self.board_type = 'BCM'
        self.relay_pin = self.config.gpio_pin
        
        if (self.config.use_direction_control):

            if (not self.config.is_low_voltage_trigger):
                raise Exception('Direction control is only supported for low voltage trigger relays.')
            
            self.switch_method = SwitchMethod.Direction
        
        self.gpio_level = self.__get_gpio_level(OnOffStatus.Off)
        GPIO.setup(self.relay_pin, self.gpio_direction, initial=self.gpio_status)

        print(f'Initialized >> {self}')

    def cleanup(self):
        GPIO.cleanup()

    def __str__(self):
        return f'{super().__str__()} | Board Type = [{self.board_type}] | GPIO Pin = [{self.relay_pin}] | Switch Method = [{self.switch_method}] (GPIO Level = [{self.gpio_level}] | GPIO Direction = [{self.direction}])' 
