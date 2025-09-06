from pydantic import BaseModel
from typing import Optional

from peripherals.actuators.relay_switches.relay_status import RelayStatus
from peripherals.sensors.tds_sensors.tds_drivers import TDSDrivers


class RelayConfig(BaseModel):

    default_status: RelayStatus = None
    gpio_pin: int = None
    driver: Optional[TDSDrivers] = None
    name: str = None

    @staticmethod
    def create(name:str, default_status: RelayStatus, gpio_pin:int, driver:Optional[TDSDrivers]):

        config_instance = RelayConfig()
        config_instance.default_status = default_status
        config_instance.gpio_pin = gpio_pin
        config_instance.driver = driver if driver is not None else TDSDrivers.Default
        config_instance.name = name

        return config_instance
