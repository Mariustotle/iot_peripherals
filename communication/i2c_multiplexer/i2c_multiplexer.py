from abc import abstractmethod
from typing import List

from peripherals.communication.communication import Communication
from peripherals.communication.communication_type import CommunicationType
from peripherals.communication.i2c_multiplexer.config import I2CMultiplexerConfig
from peripherals.communication.i2c_multiplexer.connection import MultiplexerConnection

class I2CMultiplexer(Communication):    
    config:I2CMultiplexerConfig = None
    simulated:bool = None
    connections:List[MultiplexerConnection] = None
    
    def __init__(self, config:I2CMultiplexerConfig, simulated:bool = False):
        super().__init__(CommunicationType.IOExpander, config.name)
        
        self.config = config
        self.simulated = simulated 
        self.connections = []

        if (not self.validate(config)):
            raise Exception(f'Unable to instanciate communication driver [{self.driver_name}] as the config validation failed.')        

    # Can be overrided in driver specific implimentation for special rules
    def validate(self, config:I2CMultiplexerConfig) -> bool:  return True

    def add_connection(self, connection:MultiplexerConnection) -> None:
        if connection is not None:
            for c in self.connections:
                if c.address == connection.address and c.channel == connection.channel:
                    raise Exception(f"Connection with address [{connection.address}] and channel [{connection.channel}] already exists in multiplexer for [{c.device}] cannot add a new one for [{connection.device}].")
     
            self.connections.append(connection)

    def get_description(self) -> str: 
        return f"Peripheral: [{self.peripheral_type.name}], Communication: [{self.communication_type.name}], Name: [{self.name}] with configuration of XXXXXXXX."