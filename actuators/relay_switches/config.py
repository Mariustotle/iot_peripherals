from typing import Optional
from peripherals.actuators.relay_switches.relay_drivers import RelayDrivers
from peripherals.contracts.configuration.config_base import ConfigBase
from peripherals.contracts.on_off_status import OnOffStatus
from peripherals.contracts.pins.pin_config import PinConfig

class RelayConfig(ConfigBase):
    name: str = None
    driver: Optional[RelayDrivers] = None
    default_power_status: OnOffStatus = OnOffStatus.Off
    gpio_pin: Optional[PinConfig] = None
    is_low_voltage_trigger: bool = True
    use_direction_control: bool = False