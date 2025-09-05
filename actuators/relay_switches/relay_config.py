from peripherals.actuators.relay_switches.relay_status import RelayStatus

class RelayConfig():

    default_status: RelayStatus = None
    gpio_pin: int = None

    @staticmethod
    def create(default_status: RelayStatus, gpio_pin:int):

        config_instance = RelayConfig()
        config_instance.default_status = default_status
        config_instance.gpio_pin = gpio_pin

        return config_instance
