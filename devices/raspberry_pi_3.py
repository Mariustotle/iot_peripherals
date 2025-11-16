from peripherals.contracts.device_type import DeviceType
from peripherals.contracts.pins.gpio_pin_details import GpioPinDetails
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.contracts.pins.pin_types import PinType
from peripherals.devices.adapters.adapter_base import AdapterBase
from peripherals.devices.device_base import DeviceBase
from typing import Dict


class RaspberryPi3(DeviceBase):

    def __init__(self, device_type:DeviceType, adapter:AdapterBase, default_pin_type:PinType):
        super().__init__(device_type=device_type, adapter=adapter, default_pin_type=default_pin_type)


    @staticmethod
    def get_pin_layout(adapter:AdapterBase) -> Dict[PinPosition, GpioPinDetails]:

        spi_0_feature = adapter.build_spi_feature(0)
        spi_1_feature = adapter.build_spi_feature(1)

        i2c_0_feature = adapter.build_i2c_feature(0)
        i2c_1_feature = adapter.build_i2c_feature(1)

        uart_feature = adapter.build_uart_feature()

        pin_list:Dict[PinPosition, GpioPinDetails] = {
            PinPosition.create(vertical_pos=1, horizontal_pos=1):   GpioPinDetails.create(standard_mode=PinType.Ground, board_pin=39, name='GND'),
            PinPosition.create(vertical_pos=1, horizontal_pos=2):   GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=37, gpio_pin=26),
            PinPosition.create(vertical_pos=1, horizontal_pos=3):   GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=35, gpio_pin=19, special_mode=PinType.SPI_MISO, feature=spi_1_feature),
            PinPosition.create(vertical_pos=1, horizontal_pos=4):   GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=33, gpio_pin=13, name='PWM1'),
            PinPosition.create(vertical_pos=1, horizontal_pos=5):   GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=31, gpio_pin=6, name='GPCLK2'),
            PinPosition.create(vertical_pos=1, horizontal_pos=6):   GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=29, gpio_pin=5, name='GPCLK1'),
            PinPosition.create(vertical_pos=1, horizontal_pos=7):   GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=27, gpio_pin=0, special_mode=PinType.I2C_SDA, feature=i2c_0_feature),
            PinPosition.create(vertical_pos=1, horizontal_pos=8):   GpioPinDetails.create(standard_mode=PinType.Ground, board_pin=25, name='GND'),
            PinPosition.create(vertical_pos=1, horizontal_pos=9):   GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=23, gpio_pin=11, special_mode=PinType.SPI_SCLK, feature=spi_0_feature),
            PinPosition.create(vertical_pos=1, horizontal_pos=10):  GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=21, gpio_pin=9, special_mode=PinType.SPI_MISO, feature=spi_0_feature),
            PinPosition.create(vertical_pos=1, horizontal_pos=11):  GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=19, gpio_pin=10, special_mode=PinType.SPI_MOSI, feature=spi_0_feature),
            PinPosition.create(vertical_pos=1, horizontal_pos=12):  GpioPinDetails.create(standard_mode=PinType.Power3V, board_pin=17, name='3.3V'),
            PinPosition.create(vertical_pos=1, horizontal_pos=13):  GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=15, gpio_pin=22),
            PinPosition.create(vertical_pos=1, horizontal_pos=14):  GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=13, gpio_pin=27),
            PinPosition.create(vertical_pos=1, horizontal_pos=15):  GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=11, gpio_pin=17),
            PinPosition.create(vertical_pos=1, horizontal_pos=16):  GpioPinDetails.create(standard_mode=PinType.Ground, board_pin=9, name='GND'),
            PinPosition.create(vertical_pos=1, horizontal_pos=17):  GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=7, gpio_pin=4, name='GPCLK0'),
            PinPosition.create(vertical_pos=1, horizontal_pos=18):  GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=5, gpio_pin=3, special_mode=PinType.I2C_SCL, feature=i2c_1_feature),
            PinPosition.create(vertical_pos=1, horizontal_pos=19):  GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=3, gpio_pin=2, special_mode=PinType.I2C_SDA, feature=i2c_1_feature),
            PinPosition.create(vertical_pos=1, horizontal_pos=20):  GpioPinDetails.create(standard_mode=PinType.Power3V, board_pin=1, name='3.3V'),

            PinPosition.create(vertical_pos=2, horizontal_pos=1):   GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=40, gpio_pin=21, special_mode=PinType.SPI_SCLK, feature=spi_1_feature),
            PinPosition.create(vertical_pos=2, horizontal_pos=2):   GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=38, gpio_pin=20, special_mode=PinType.SPI_MOSI, feature=spi_1_feature),
            PinPosition.create(vertical_pos=2, horizontal_pos=3):   GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=36, gpio_pin=16),
            PinPosition.create(vertical_pos=2, horizontal_pos=4):   GpioPinDetails.create(standard_mode=PinType.Ground, board_pin=34, name='GND'),
            PinPosition.create(vertical_pos=2, horizontal_pos=5):   GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=32, gpio_pin=12, name='PWM0'),
            PinPosition.create(vertical_pos=2, horizontal_pos=6):   GpioPinDetails.create(standard_mode=PinType.Ground, board_pin=30, name='GND'),
            PinPosition.create(vertical_pos=2, horizontal_pos=7):   GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=28, gpio_pin=1, special_mode=PinType.I2C_SCL, feature=i2c_0_feature),
            PinPosition.create(vertical_pos=2, horizontal_pos=8):   GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=26, gpio_pin=7, special_mode=PinType.SPI_CE1, feature=spi_0_feature),
            PinPosition.create(vertical_pos=2, horizontal_pos=9):   GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=24, gpio_pin=8, special_mode=PinType.SPI_CE0, feature=spi_0_feature),
            PinPosition.create(vertical_pos=2, horizontal_pos=10):  GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=22, gpio_pin=25),
            PinPosition.create(vertical_pos=2, horizontal_pos=11):  GpioPinDetails.create(standard_mode=PinType.Ground, board_pin=20, name='GND'),
            PinPosition.create(vertical_pos=2, horizontal_pos=12):  GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=18, gpio_pin=24),
            PinPosition.create(vertical_pos=2, horizontal_pos=13):  GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=16, gpio_pin=23),
            PinPosition.create(vertical_pos=2, horizontal_pos=14):  GpioPinDetails.create(standard_mode=PinType.Ground, board_pin=14, name='GND'),
            PinPosition.create(vertical_pos=2, horizontal_pos=15):  GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=12, gpio_pin=18, name='PWM0'),
            PinPosition.create(vertical_pos=2, horizontal_pos=16):  GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=10, gpio_pin=15, special_mode=PinType.UART_RX, name='RXD', feature=uart_feature),
            PinPosition.create(vertical_pos=2, horizontal_pos=17):  GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=8, gpio_pin=14, special_mode=PinType.UART_TX, name='TXD', feature=uart_feature),
            PinPosition.create(vertical_pos=2, horizontal_pos=18):  GpioPinDetails.create(standard_mode=PinType.Ground, board_pin=6, name='GND'),
            PinPosition.create(vertical_pos=2, horizontal_pos=19):  GpioPinDetails.create(standard_mode=PinType.Power5V, board_pin=4, name='5V'),
            PinPosition.create(vertical_pos=2, horizontal_pos=20):  GpioPinDetails.create(standard_mode=PinType.Power5V, board_pin=2, name='5V')
        }

        return pin_list

        
        
       
