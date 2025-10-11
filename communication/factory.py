from typing import Any

from peripherals.communication.analog_digital_converter.adc_module import ADCModule
from peripherals.communication.analog_digital_converter.config import ADCConfig
from peripherals.communication.i2c_multiplexer.config import I2CMultiplexerConfig
from peripherals.communication.i2c_multiplexer.i2c_multiplexer import I2CMultiplexer

class CommunicationFactory():

    def create(self, config:Any, simulate:bool = False) -> 'Any':
            
        if (isinstance(config, I2CMultiplexerConfig)):
            return I2CMultiplexer(config, simulate)
        
        if (isinstance(config, ADCConfig)):
            return ADCModule(config, simulate)
        
        raise Exception(f"Unsupported communication config type: {type(config)}")