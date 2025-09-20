from abc import abstractmethod

from peripherals.actuators.action_decorator import action
from peripherals.actuators.actuator import Actuator
from peripherals.actuators.actuator_types import ActuatorType
from peripherals.actuators.relay_switches.relay_config import RelayConfig
from peripherals.actuators.relay_switches.relay_drivers import RelayDrivers
from peripherals.actuators.relay_switches.relay_status import RelayStatus

class RelayDriverBase(Actuator):    
    config:RelayConfig = None
    simulated:bool = None
    relay_pin:int = None

    
    def __init__(self, config:RelayConfig, simulated:bool = False):
        driver = config.driver if config.driver is not None else RelayDrivers.Default
        driver_name = driver.value if not simulated else 'N/A - Simulated'

        super().__init__(ActuatorType.Relay, config.name, driver_name, status=config.default_status)
        
        self.config = config
        self.simulated = simulated 
        self.relay_pin = config.gpio_pin        

        if (not self.validate(config)):
            raise Exception(f'Unable to instanciate Relay Driver [{self.driver_name}] as the config validation failed.')        

    # Can be overrided in driver specific implimentation for special rules
    def validate(self, config:RelayConfig) -> bool:  return True

    @abstractmethod
    def _switch_on(self):  pass

    @abstractmethod
    def _switch_off(self):  pass

    def get_current_status(self) -> 'RelayStatus':
        return self.status

    @action(label="Switch to On/OFF", description="Set relay to a specific state")    
    def switch(self, status:RelayStatus):
        if self.status == status:
            return
        
        if self.status == None:
            if status == RelayStatus.On:
                self.switch_on()
            else:
                self.switch_off()
                
        else:
            self.toggle()     

    @action(label="Switch On", description="Set relay to an On state")    
    def switch_on(self) -> 'RelayStatus':
        try:
            self._switch_on()
            self.status = RelayStatus.On

        except Exception as ex:
            print(f"Oops! {ex.__class__} occurred while trying to switch [{self.driver_name}] on. Details: {ex}")

        return self.status

    @action(label="Switch OFF", description="Set relay to an OFF state")    
    def switch_off(self) -> 'RelayStatus':
        try:
            self._switch_off()
            self.status = RelayStatus.Off

        except Exception as ex:
            print(f"Oops! {ex.__class__} occurred while trying to switch [{self.driver_name}] off. Details: {ex}")

        return self.status
    
    @action(label="Toggle to the opposite", description="Set relay state to the opposite that it is currently") 
    def toggle(self):
        try:
            
            switch_on = True if self.status == RelayStatus.Off else False
            if switch_on:
                self.switch_on()
            else:
                self.switch_off()

        except Exception as ex:
            print(f"Oops! {ex.__class__} occurred while trying to switch [{self.driver_name}] off. Details: {ex}")

        return self.status

    def get_description(self) -> str: 
        return f"Peripheral: [{self.peripheral_type.name}], Actuator: [{self.actuator_type.name}], Driver: [{self.driver_name}] with configuration of GPIO Pin [{self.config.gpio_pin}] with default status of [{self.config.default_status.value}]."