from enum import Enum

class PinType(str, Enum):
    Default = "default"
    DIGITAL = "digital"
    ANALOG = "analog"
    I2C_SDA = "i2c_sda"
    I2C_SCL = "i2c_scl"
    UART_TX = "uart_tx"
    UART_RX = "uart_rx"
    SPI_MOSI = "spi_mosi"
    SPI_MISO = "spi_miso"
    SPI_SCLK = "spi_sclk"
    SPI_CE0 = "spi_ce0"
    SPI_CE1 = "spi_ce1"
    PWM_AUDIO_PCM_CLK = "pwm_audio_pcm_clk"
    PWM_0 = "pwm_0"
    PWM_1 = "pwm_1"
    EEPROM_SD = "eeprom_sd"
    EEPROM_SC = "eeprom_sc"
    ONEWIRE = "onewire"

