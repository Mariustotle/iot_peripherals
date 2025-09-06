from abc import abstractmethod

from peripherals.communication.analog_digital_converter.adc_drivers import ADCDrivers
from peripherals.communication.communication import Communication
from peripherals.communication.communication_type import CommunicationType
from peripherals.communication.analog_digital_converter.adc_config import ADCConfig

class ADCDriverBase(Communication):    
    config:ADCConfig = None
    simulated:bool = None
    
    def __init__(self, config:ADCConfig, simulated:bool = False):
        driver = config.driver if config.driver is not None else ADCDrivers.Default
        driver_name = driver.value if not simulated else 'N/A - Simulated'

        super().__init__(CommunicationType.AnologDigitalConverter, config.name, driver_name)
        
        self.config = config
        self.simulated = simulated 

        if (not self.validate(config)):
            raise Exception(f'Unable to instanciate communication driver [{self.driver_name}] as the config validation failed.')        

    # Can be overrided in driver specific implimentation for special rules
    def validate(self, config:ADCConfig) -> bool:  return True


    def get_description(self) -> str: 
        return f"Peripheral: [{self.peripheral_type.name}], Communication: [{self.communication_type.name}], Driver: [{self.driver_name}] with configuration of XXXXXXXX."