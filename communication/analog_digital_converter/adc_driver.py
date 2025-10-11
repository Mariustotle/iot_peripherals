from abc import abstractmethod
from typing import List
from peripherals.communication.analog_digital_converter.connection import ADCConnection
from peripherals.communication.communication import Communication
from peripherals.communication.communication_type import CommunicationType
from peripherals.communication.analog_digital_converter.config import ADCConfig

class ADCDriver(Communication):    
    config:ADCConfig = None
    simulated:bool = None
    connections:List[ADCConnection] = None
    
    def __init__(self, config:ADCConfig, simulated:bool = False):

        super().__init__(CommunicationType.AnologDigitalConverter, config.name)
        
        self.config = config
        self.simulated = simulated
        self.connections = []

        if (not self.validate(config)):
            raise Exception(f'Unable to instanciate communication driver [{self.driver_name}] as the config validation failed.')        

    # Can be overrided in driver specific implimentation for special rules
    def validate(self, config:ADCConfig) -> bool:  return True

    def add_connection(self, connection:ADCConnection) -> None:
        if connection is not None:
            # Check that this connection does not already exist
            '''
               for c in self.connections:
                if c.address == connection.address and c.channel == connection.channel:
                    raise Exception(f"Connection with address [{connection.address}] and channel [{connection.channel}] already exists in multiplexer for [{c.device}] cannot add a new one for [{connection.device}].")
            '''
            
            raise Exception("Not implemented yet")
            # self.connections.append(connection)

    def get_description(self) -> str: 
        return f"Peripheral: [{self.peripheral_type.name}], Communication: [{self.communication_type.name}], Name: [{self.name}] with configuration of XXXXXXXX."