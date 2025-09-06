from pydantic import BaseModel
from typing import Optional
from peripherals.communication.analog_digital_converter.adc_drivers import ADCDrivers

class ADCConfig(BaseModel):
    name: str = None
    driver: Optional[ADCDrivers] = None
    spi_bus: int = None
    spi_device: int = None
    channel: int = None
    
    


