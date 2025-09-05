from peripherals.actuators.relay_switches.relay_status import RelayStatus

class RelayConfig:

    default_status: RelayStatus = None
    gpio_pin: int = None

    def __init__(self, default_status: RelayStatus, gpio_pin:int):
        self.default_status = default_status
        self.gpio_pin = gpio_pin