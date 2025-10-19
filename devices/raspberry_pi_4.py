

from typing import List, Optional
from peripherals.contracts.device_type import DeviceType
from peripherals.contracts.pins.pin_number import PinNumber
from peripherals.contracts.pins.pin_types import PinType
from peripherals.devices.device_base import DeviceBase
from peripherals.devices.device_feature import DeviceFeature

class RaspberryPi4(DeviceBase):
    def __init__(self):
        super().__init__(DeviceType.RaspberryPi3, PinType.DIGITAL)



    def check_i2c_config(self):

        # check device directly - placeholder
        is_i2c_enabled = True
        feature = DeviceFeature.create("I2C", True, is_i2c_enabled)        
        
        if (feature.enabled):
            feature.add_associated_pin(PinNumber(2, 3), PinType.I2C_SDA)
            feature.add_associated_pin(PinNumber(2, 3), PinType.I2C_SCL)



    def configure_available_pins(self) -> dict[PinNumber, Optional[List[PinType]]]:

        available_pins = {
            PinNumber(4, 7):    [PinType.DIGITAL],
            PinNumber(14, 8):   [PinType.DIGITAL, PinType.UART_TX],
            PinNumber(15, 10):  [PinType.DIGITAL, PinType.UART_RX],
            PinNumber(18, 12):  [PinType.DIGITAL, PinType.PWM_0],
            PinNumber(19, 35):  [PinType.DIGITAL, PinType.SPI_MOSI],
            PinNumber(20, 38):  [PinType.DIGITAL, PinType.SPI_MISO],
            PinNumber(21, 40):  [PinType.DIGITAL, PinType.SPI_SCLK],
            PinNumber(8, 24):   [PinType.DIGITAL, PinType.SPI_CE0],
            PinNumber(7, 26):   [PinType.DIGITAL, PinType.SPI_CE1],
            PinNumber(12, 32):  [PinType.DIGITAL, PinType.PWM_0],
            PinNumber(13, 33):  [PinType.DIGITAL, PinType.PWM_1],
            PinNumber(27, 13):  [PinType.DIGITAL],
            PinNumber(22, 15):  [PinType.DIGITAL],
            PinNumber(17, 11):  [PinType.DIGITAL],
        }


        i2c_feature = self.check_i2c_config()
         
    
