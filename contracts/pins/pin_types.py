from enum import Enum
from typing import Optional

class PinType(str, Enum):
    def __new__(cls, value: str, short: str, description: Optional[str] = None):
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj.short = short
        obj.description = description

        return obj

    def __str__(self):
        return self.value  # Default string representation

    # Optional helper for reverse lookup
    @classmethod
    def from_short(cls, short: str):
        return next((e for e in cls if e.short == short), None)

    Default =               ("Default",             "DEF")
    Ground =                ("Ground",              "GND")
    Power3V =               ("Power (3V)",          "3V3")
    Power5V =               ("Power (5V)",          "5V")
    DIGITAL =               ("Digital",             "DTA")
    ANALOG =                ("Analog",              "SIG")
    I2C_SDA =               ("I2C-SDA",             "SDA")
    I2C_SCL =               ("I2C-SCL",             "SCL")
    UART_TX =               ("UART-TX",             "TX")
    UART_RX =               ("UART-RX",             "RX")
    SPI_MOSI =              ("SPI-MOSI",            "MOSI")
    SPI_MISO =              ("SPI-SO",              "MISO")
    SPI_SCLK =              ("SPI-SCLK",            "SCLK")
    SPI_CE0 =               ("SPI-CE-0",            "CE0")
    SPI_CE1 =               ("SPI-CE-1",            "CE1")
    PWM_AUDIO_PCM_CLK =     ("pwm_audio_pcm_clk",   "CLK")
    PWM_0 =                 ("PWM-0",               "PWM0")
    PWM_1 =                 ("PWM-1",               "PWM1")
    EEPROM_SD =             ("EEPROM-SD",           "ESD")
    EEPROM_SC =             ("EEPROM-SC",           "ESC")
    ONEWIRE =               ("ONEWIRE",             "1W")
