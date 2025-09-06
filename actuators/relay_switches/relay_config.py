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

    @staticmethod
    def create(name:str, default_status: RelayStatus, gpio_pin:int, driver:Optional[RelayDrivers]):

        config_instance = RelayConfig()
        config_instance.default_status = default_status
        config_instance.gpio_pin = gpio_pin
        config_instance.driver = driver if driver is not None else RelayDrivers.Default
        config_instance.name = name

        return config_instance
