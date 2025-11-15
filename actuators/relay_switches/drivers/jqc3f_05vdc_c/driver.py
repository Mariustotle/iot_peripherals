
from typing import Literal, Optional
import RPi.GPIO as GPIO

from peripherals.actuators.relay_switches.config import RelayConfig
from peripherals.actuators.relay_switches.driver_base import RelayDriverBase
from peripherals.contracts.gpio_status import GPIOStatus
from peripherals.contracts.input_output import InputOutput
from peripherals.contracts.on_off_status import OnOffStatus
from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.contracts.pins.pin_types import PinType
from peripherals.contracts.switch_method import SwitchMethod
from peripherals.peripheral_type import PeripheralType

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


    def _initialize(self, name:str, config:Optional[RelayConfig] = None) -> bool:

        GPIO.setmode(GPIO.BCM)   # BCM pin numbering
        self.board_type = 'BCM'
        self.relay_pin = config.gpio_pin.pin

        if (config.use_direction_control and not config.is_low_voltage_trigger):
            raise Exception('Direction control is only supported for low voltage trigger relays.')
        
        self.switch_method = SwitchMethod.Level if not config.use_direction_control else SwitchMethod.Direction
        self.direction = InputOutput.Output if not config.use_direction_control else self.__get_gpio_direction(config.default_power_status)
        
        self.gpio_level = self.__get_gpio_level(OnOffStatus.Off)
        print(f'Initializing {self.name} on GPIO Pin {self.relay_pin} using [{self.switch_method}] method with [{self.gpio_level}] level and [{self.direction}] direction.')

        if (self.switch_method == SwitchMethod.Level):
            GPIO.setup(self.relay_pin, GPIO.OUT, initial=self.gpio_status)
        else: 
            self._set_relay_properties(OnOffStatus.Off)

        return True
    
    
    def configure_available_pins(self):
        
        self.add_pin(
            pin_position=PinPosition.create(horizontal_pos=1),
            pin_details=PinDetails.create(type=PinType.Power3V, name='VCC')            
        )

        self.add_pin(
            pin_position=PinPosition.create(horizontal_pos=2),
            pin_details=PinDetails.create(type=PinType.Ground, name='GND')            
        )
        
        self.add_pin(
            pin_position=PinPosition.create(horizontal_pos=3),
            pin_details=PinDetails.create(type=PinType.ANALOG, name='IN')            
        )


    def cleanup(self):
        GPIO.cleanup()

    def __str__(self):
        return f'{super().__str__()} | Board Type = [{self.board_type}] | GPIO Pin = [{self.relay_pin}] | Switch Method = [{self.switch_method}] (GPIO Level = [{self.gpio_level}] | GPIO Direction = [{self.direction}])' 
