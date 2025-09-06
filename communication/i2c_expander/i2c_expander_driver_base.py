from abc import abstractmethod

from peripherals.communication.communication import Communication
from peripherals.communication.communication_type import CommunicationType
from peripherals.communication.i2c_expander.i2c_expander_config import I2CExpanderConfig


class I2CExpanderDriverBase(Communication):    
    config:I2CExpanderConfig = None
    simulated:bool = None
    
    def __init__(self, config:I2CExpanderConfig, simulated:bool = False):
        driver_name = config.driver.value if not simulated else 'N/A - Simulated'

        super().__init__(CommunicationType.IOExpander, config.name, driver_name)
        
        self.config = config
        self.simulated = simulated 

        if (not self.validate(config)):
            raise Exception(f'Unable to instanciate communication driver [{self.driver_name}] as the config validation failed.')        

    # Can be overrided in driver specific implimentation for special rules
    def validate(self, config:I2CExpanderConfig) -> bool:  return True


    def get_description(self) -> str: 
        return f"Peripheral: [{self.peripheral_type.name}], Communication: [{self.communication_type.name}], Driver: [{self.driver_name}] with configuration of XXXXXXXX."