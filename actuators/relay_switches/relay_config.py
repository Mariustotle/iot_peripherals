from pydantic import BaseModel
from typing import Optional
from peripherals.actuators.relay_switches.relay_drivers import RelayDrivers
from peripherals.contracts.on_off_status import OnOffStatus

class RelayConfig(BaseModel):
    name: str = None
    driver: Optional[RelayDrivers] = None
    default_power_status: OnOffStatus = None
    gpio_pin: int = None
    is_low_voltage_trigger: bool = None