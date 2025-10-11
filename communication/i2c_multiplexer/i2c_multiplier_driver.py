from abc import abstractmethod

from peripherals.communication.communication import Communication
from peripherals.communication.communication_type import CommunicationType
from peripherals.communication.i2c_multiplexer.config import I2CMultiplexerConfig

class I2CExpanderDriver(Communication):    
    config:I2CMultiplexerConfig = None
    simulated:bool = None
    
    def __init__(self, config:I2CMultiplexerConfig, simulated:bool = False):
        super().__init__(CommunicationType.IOExpander, config.name)
        
        self.config = config
        self.simulated = simulated 

        if (not self.validate(config)):
            raise Exception(f'Unable to instanciate communication driver [{self.driver_name}] as the config validation failed.')        

    # Can be overrided in driver specific implimentation for special rules
    def validate(self, config:I2CMultiplexerConfig) -> bool:  return True


    def get_description(self) -> str: 
        return f"Peripheral: [{self.peripheral_type.name}], Communication: [{self.communication_type.name}], Name: [{self.name}] with configuration of XXXXXXXX."