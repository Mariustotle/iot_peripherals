from pydantic import BaseModel
from typing import Optional

class ADCConfig(BaseModel):
    name: str = None
    spi_bus: int = None
    spi_device: int = None
    channel: int = None
    
    


