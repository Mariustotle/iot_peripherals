from enum import Enum

class PinType(str, Enum):
    def __new__(cls, value: str, short: str):
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj.short = short
        return obj

    def __str__(self):
        return self.value  # Default string representation

    # Optional helper for reverse lookup
    @classmethod
    def from_short(cls, short: str):
        return next((e for e in cls if e.short == short), None)

    Default = ("default", "DEF")
    Ground = ("ground", "GND")
    Power3V = ("power_3.3v", "3V3")
    Power5V = ("power_5v", "5V")
    DIGITAL = ("digital", "DTA")
    ANALOG = ("analog", "SIG")
    I2C_SDA = ("i2c_sda", "SDA")
    I2C_SCL = ("i2c_scl", "SCL")
    UART_TX = ("uart_tx", "TX")
    UART_RX = ("uart_rx", "RX")
    SPI_MOSI = ("spi_mosi", "MOSI")
    SPI_MISO = ("spi_miso", "MISO")
    SPI_SCLK = ("spi_sclk", "SCLK")
    SPI_CE0 = ("spi_ce0", "CE0")
    SPI_CE1 = ("spi_ce1", "CE1")
    PWM_AUDIO_PCM_CLK = ("pwm_audio_pcm_clk", "CLK")
    PWM_0 = ("pwm_0", "PWM0")
    PWM_1 = ("pwm_1", "PWM1")
    EEPROM_SD = ("eeprom_sd", "ESD")
    EEPROM_SC = ("eeprom_sc", "ESC")
    ONEWIRE = ("onewire", "1W")
