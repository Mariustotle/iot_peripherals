from pydantic import BaseModel
from typing import Optional
from peripherals.communication.analog_digital_converter.adc_drivers import ADCDrivers

class ADCConfig(BaseModel):
    gpio_a0: int = None
    gpio_a1: int = None
    gpio_a2: int = None
    gpio_a3: int = None
    driver: Optional[ADCDrivers] = None
    name: str = None


