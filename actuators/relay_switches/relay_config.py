from pydantic import BaseModel
from typing import Optional
from peripherals.actuators.relay_switches.relay_drivers import RelayDrivers
from peripherals.actuators.relay_switches.relay_status import RelayStatus

class RelayConfig(BaseModel):
    driver_name:str = None
    default_status: RelayStatus = None
    gpio_pin: int = None
    driver: Optional[RelayDrivers] = None
    name: str = None
