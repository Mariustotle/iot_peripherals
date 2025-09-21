
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
    switch_method:SwitchMethod = SwitchMethod.Undefined
    direction:InputOutput = InputOutput.Undefined

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
        
        if relay_status == OnOffStatus.On:
            return InputOutput.Output
        else:
            return InputOutput.Input

       
    def __init__(self, config:RelayConfig, simulated = False):
        super().__init__(config, simulated) 


    def _set_relay_properties(self, relay_status:OnOffStatus):

        # First set direction in case it is output
        if (self.switch_method == SwitchMethod.Direction):

            # If changing from off to on, set level first before changing direction
            if (relay_status == OnOffStatus.Off and self.relay_status == OnOffStatus.On):
                self.relay_status = relay_status
                self.gpio_level = self.__get_gpio_level(self.relay_status)
                GPIO.output(self.relay_pin, self.gpio_status)

            self.direction = self.__get_gpio_direction(relay_status)
            GPIO.setup(self.relay_pin, self.gpio_direction)

            if (self.direction == InputOutput.Input):
                return  # If input, do not change level (Not allowed for INPUT)
        
        self.relay_status = relay_status
        self.gpio_level = self.__get_gpio_level(self.relay_status)
        GPIO.output(self.relay_pin, self.gpio_status)


    def initialize(self) -> bool:

        try:

            GPIO.setmode(GPIO.BCM)   # BCM pin numbering
            self.board_type = 'BCM'
            self.relay_pin = self.config.gpio_pin            

            if (self.config.use_direction_control and not self.config.is_low_voltage_trigger):
                raise Exception('Direction control is only supported for low voltage trigger relays.')
            
            self.switch_method = SwitchMethod.Level if not self.config.use_direction_control else SwitchMethod.Direction
            self.direction = InputOutput.Output if not self.config.use_direction_control else self.__get_gpio_direction(self.config.default_power_status)
            
            self.gpio_level = self.__get_gpio_level(OnOffStatus.Off)
            print(f'Initializing {self.name} on GPIO Pin {self.relay_pin} using [{self.switch_method}] method with [{self.gpio_level}] level and [{self.direction}] direction.')

            if (self.switch_method == SwitchMethod.Level):
                GPIO.setup(self.relay_pin, GPIO.OUT, initial=self.gpio_status)
            else: 
                self._set_relay_properties(self.config.default_power_status, OnOffStatus.Off)

            return True

        except Exception as ex:
            print(f"Oops! {ex.__class__} Unable to intialize [{self.driver_name}]. Details: {ex}")

        return False


    def cleanup(self):
        GPIO.cleanup()

    def __str__(self):
        return f'{super().__str__()} | Board Type = [{self.board_type}] | GPIO Pin = [{self.relay_pin}] | Switch Method = [{self.switch_method}] (GPIO Level = [{self.gpio_level}] | GPIO Direction = [{self.direction}])' 
