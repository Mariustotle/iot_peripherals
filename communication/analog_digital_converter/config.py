from pydantic import BaseModel
from typing import Optional

class ADCConfig(BaseModel):
    name: str = None
    gpio_pin: Optional[int] = None
    
    


