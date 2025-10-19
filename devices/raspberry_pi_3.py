
from peripherals.contracts.device_type import DeviceType
from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_types import PinType
from peripherals.devices.device_base import DeviceBase
from peripherals.devices.device_feature import DeviceFeature


class RaspberryPi3(DeviceBase):
    def __init__(self):
        super().__init__(DeviceType.RaspberryPi3, PinType.DIGITAL)


    def _build_i2c_feature(self) -> 'DeviceFeature':
        # check device directly - placeholder
        is_i2c_enabled = True

        feature = DeviceFeature.create("I2C", True, is_i2c_enabled)
        return feature    

    def _build_uart_feature(self) -> 'DeviceFeature':
        # check device directly - placeholder
        is_uart_enabled = True

        feature = DeviceFeature.create("UART", True, is_uart_enabled)
        return feature
    
    def _build_spi_feature(self) -> 'DeviceFeature':
        # check device directly - placeholder
        is_spi_enabled = True

        feature = DeviceFeature.create("SPI", True, is_spi_enabled)
        return feature
    
    def _build_pwm_feature(self) -> 'DeviceFeature':
        # check device directly - placeholder
        is_pwm_enabled = True

        feature = DeviceFeature.create("PWM", True, is_pwm_enabled)
        return feature 


    def configure_available_pins(self):
        
        # I2C
        i2c_feature = self._build_i2c_feature()
        self.add_pin(gpio_number=2,     board_number=3,     special_mode=PinType.I2C_SDA,   feature=i2c_feature)
        self.add_pin(gpio_number=3,     board_number=5,     special_mode=PinType.I2C_SCL,   feature=i2c_feature)

        # UART
        uart_feature = self._build_uart_feature()
        self.add_pin(gpio_number=14,     board_number=8,     special_mode=PinType.UART_TX,   feature=uart_feature)
        self.add_pin(gpio_number=15,     board_number=10,    special_mode=PinType.UART_RX,   feature=uart_feature)

        # SPI
        spi_feature = self._build_spi_feature()
        self.add_pin(gpio_number=23,     board_number=16,     special_mode=PinType.SPI_SCLK,   feature=spi_feature)
        self.add_pin(gpio_number=24,     board_number=18,     special_mode=PinType.SPI_CE0,   feature=spi_feature)
        self.add_pin(gpio_number=8,      board_number=24,     special_mode=PinType.SPI_CE0,   feature=spi_feature)
        self.add_pin(gpio_number=9,      board_number=21,     special_mode=PinType.SPI_MISO,   feature=spi_feature)
        self.add_pin(gpio_number=109,    board_number=19,     special_mode=PinType.SPI_MOSI,   feature=spi_feature)
        self.add_pin(gpio_number=11,     board_number=23,     special_mode=PinType.SPI_SCLK,   feature=spi_feature)
        self.add_pin(gpio_number=26,     board_number=37,     special_mode=PinType.SPI_CE1,   feature=spi_feature)

        # PWM
        pwm_feature = self._build_pwm_feature()
        self.add_pin(gpio_number=18,     board_number=12,     special_mode=PinType.PWM_0,   feature=pwm_feature)
        self.add_pin(gpio_number=12,     board_number=32,     special_mode=PinType.PWM_0,   feature=pwm_feature)
        self.add_pin(gpio_number=13,     board_number=33,     special_mode=PinType.PWM_0,   feature=pwm_feature)

        # Standard Pins
        self.add_pin(gpio_number=4,     board_number=7)
        self.add_pin(gpio_number=25,    board_number=22)
