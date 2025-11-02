
from peripherals.contracts.pins.gpio_pin_details import GpioPinDetails
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.contracts.pins.pin_types import PinType
from peripherals.devices.device_base import DeviceBase


class RaspberryPi3(DeviceBase):


    def configure_available_pins(self):

        spi_0_feature = self.adapter.build_spi_feature()
        spi_1_feature = self.adapter.build_spi_feature()

        i2c_0_feature = self.adapter.build_i2c_feature()
        i2c_1_feature = self.adapter.build_i2c_feature()

        # ------------------------------
        # FIRST ROW
        # ------------------------------

        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=1, horizontal_pos=1),
            pin_details=GpioPinDetails.create(standard_mode=PinType.Ground, board_pin=39, label='GND')
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=1, horizontal_pos=2),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=37, gpio_pin=26)
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=1, horizontal_pos=3),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=35, gpio_pin=19, special_mode=PinType.SPI_MISO, feature=spi_1_feature)
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=1, horizontal_pos=4),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=33, gpio_pin=13, label='PWM1')
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=1, horizontal_pos=5),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=31, gpio_pin=6, label='GPCLK2')
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=1, horizontal_pos=6),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=29, gpio_pin=5, label='GPCLK1')
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=1, horizontal_pos=7),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=27, gpio_pin=0, special_mode=PinType.I2C_SDA, feature=i2c_0_feature, label='12C0')
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=1, horizontal_pos=8),
            pin_details=GpioPinDetails.create(standard_mode=PinType.Ground, board_pin=25, label='GND')
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=1, horizontal_pos=9),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=23, gpio_pin=11, special_mode=PinType.SPI_SCLK, feature=spi_0_feature)
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=1, horizontal_pos=10),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=21, gpio_pin=9, special_mode=PinType.SPI_MISO, feature=spi_0_feature)
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=1, horizontal_pos=11),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=19, gpio_pin=10, special_mode=PinType.SPI_MOSI, feature=spi_0_feature)
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=1, horizontal_pos=12),
            pin_details=GpioPinDetails.create(standard_mode=PinType.Power3V, board_pin=17, label='3.3V')
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=1, horizontal_pos=13),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=15, gpio_pin=22)
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=1, horizontal_pos=14),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=13, gpio_pin=27)
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=1, horizontal_pos=15),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=11, gpio_pin=17)
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=1, horizontal_pos=16),
            pin_details=GpioPinDetails.create(standard_mode=PinType.Ground, board_pin=9, label='GND')
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=1, horizontal_pos=17),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=7, gpio_pin=4, label='GPCLK0')
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=1, horizontal_pos=18),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=5, gpio_pin=3, special_mode=PinType.I2C_SCL, feature=i2c_1_feature)
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=1, horizontal_pos=19),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=3, gpio_pin=2, special_mode=PinType.I2C_SDA, feature=i2c_1_feature)
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=1, horizontal_pos=20),
            pin_details=GpioPinDetails.create(standard_mode=PinType.Power3V, board_pin=1, label='3.3V')
        )

        # ------------------------------
        # SECOND ROW
        # ------------------------------
        
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=2, horizontal_pos=1),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=40, gpio_pin=21, special_mode=PinType.SPI_SCLK, feature=spi_1_feature)
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=2, horizontal_pos=2),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=38, gpio_pin=20, special_mode=PinType.SPI_MOSI, feature=spi_1_feature)
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=2, horizontal_pos=3),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=36, gpio_pin=16)
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=2, horizontal_pos=4),
            pin_details=GpioPinDetails.create(standard_mode=PinType.Ground, board_pin=34, label='GND')
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=2, horizontal_pos=5),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=32, gpio_pin=12, label='PWM0')
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=2, horizontal_pos=6),
            pin_details=GpioPinDetails.create(standard_mode=PinType.Ground, board_pin=30, label='GND')
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=2, horizontal_pos=7),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=28, gpio_pin=1, special_mode=PinType.I2C_SCL, feature=i2c_0_feature)
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=2, horizontal_pos=8),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=26, gpio_pin=7, special_mode=PinType.SPI_CE1, feature=spi_0_feature)
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=2, horizontal_pos=9),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=24, gpio_pin=8, special_mode=PinType.SPI_CE0, feature=spi_0_feature)
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=2, horizontal_pos=10),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=22, gpio_pin=25)
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=2, horizontal_pos=11),
            pin_details=GpioPinDetails.create(standard_mode=PinType.Ground, board_pin=20, label='GND')
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=2, horizontal_pos=12),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=18, gpio_pin=24)
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=2, horizontal_pos=13),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=16, gpio_pin=23)
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=2, horizontal_pos=14),
            pin_details=GpioPinDetails.create(standard_mode=PinType.Ground, board_pin=14, label='GND')
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=2, horizontal_pos=15),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=12, gpio_pin=18, label='PWM0')
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=2, horizontal_pos=16),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=10, gpio_pin=15, special_mode=PinType.UART_RX, label='RXD')
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=2, horizontal_pos=17),
            pin_details=GpioPinDetails.create(standard_mode=PinType.DIGITAL, board_pin=8, gpio_pin=14, special_mode=PinType.UART_TX, label='TXD')
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=2, horizontal_pos=18),
            pin_details=GpioPinDetails.create(standard_mode=PinType.Ground, board_pin=6, label='GND')
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=2, horizontal_pos=19),
            pin_details=GpioPinDetails.create(standard_mode=PinType.Power5V, board_pin=4, label='5V')
        )
        self.add_gpio_pin(
            pin_position=PinPosition.create(vertical_pos=2, horizontal_pos=20),
            pin_details=GpioPinDetails.create(standard_mode=PinType.Power5V, board_pin=2, label='5V')
        )
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
