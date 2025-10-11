from abc import abstractmethod
from peripherals.communication.communication import Communication
from peripherals.communication.communication_type import CommunicationType
from peripherals.communication.analog_digital_converter.config import ADCConfig

class ADCDriver(Communication):    
    config:ADCConfig = None
    simulated:bool = None
    
    def __init__(self, config:ADCConfig, simulated:bool = False):

        super().__init__(CommunicationType.AnologDigitalConverter, config.name)
        
        self.config = config
        self.simulated = simulated 

        if (not self.validate(config)):
            raise Exception(f'Unable to instanciate communication driver [{self.driver_name}] as the config validation failed.')        

    # Can be overrided in driver specific implimentation for special rules
    def validate(self, config:ADCConfig) -> bool:  return True


    def get_description(self) -> str: 
        return f"Peripheral: [{self.peripheral_type.name}], Communication: [{self.communication_type.name}], Name: [{self.name}] with configuration of XXXXXXXX."