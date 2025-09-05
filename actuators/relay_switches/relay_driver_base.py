from abc import ABC, abstractmethod


from peripherals.actuators.relay_switches.relay_config import RelayConfig
from peripherals.actuators.relay_switches.relay_status import RelayStatus


class RelayDriverBase(ABC):   
    driver:str = None
    status:RelayStatus = None
    config:RelayConfig = None
    simulated:bool = None
    
    def __init__(self, driver_name:str, config:RelayConfig, simulated:bool = False):
        self.driver = driver_name
        self.config = config
        self.simulated = simulated

        if (not self.validate(config)):
            raise Exception(f'Unable to instanciate Relay Driver [{driver_name}] as the config validation failed.')        

    # Can be overrided in driver specific implimentation for special rules
    def validate(self, config:RelayConfig) -> bool:  return True

    @abstractmethod
    def _switch_on(self):  pass

    @abstractmethod
    def _switch_off(self):  pass

    def get_current_status(self) -> 'RelayStatus':
        return self.status

    def switch_on(self) -> 'RelayStatus':
        try:
            self._switch_on()
            self.status = RelayStatus.On

        except Exception as ex:
            print(f"Oops! {ex.__class__} occurred while trying to switch [{self.driver}] on. Details: {ex}")

        return self.status

    def switch_off(self) -> 'RelayStatus':
        try:
            self._switch_off()
            self.status = RelayStatus.Off

        except Exception as ex:
            print(f"Oops! {ex.__class__} occurred while trying to switch [{self.driver}] off. Details: {ex}")

        return self.status


    def toggle(self):
        try:
            
            switch_on = True if self.status == RelayStatus.Off else False
            if switch_on:
                self.switch_on()
            else:
                self.switch_off()

        except Exception as ex:
            print(f"Oops! {ex.__class__} occurred while trying to switch [{self.driver}] off. Details: {ex}")

        return self.status


