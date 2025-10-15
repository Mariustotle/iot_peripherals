# Peripheral Index
These are the peripherals avaialble under this project.

## Sensors
These are peripherals that measure things.

Type                                                    | Description
-------------                                           | ---------------
[TDS](sensors/tds_sensors/README.md)                    | Measure particles
Digital Temprature and Humidity | [DHT11](sensors/digital_temp_sensors/drivers/dht11_README.md) / [DHT22](sensors/digital_temp_sensors/drivers/dht11_README.md) Sensors
I2C Combo Sensors | [BMP280](sensors/digital_i2c_combo_sensor/drivers/bme280_README.md) Digital Temp/Air/Humidity
Water Level | Measure when a specific water level is reached
Temperature & Humidity | Measuring the temperature and humidity


## Actuators
These are peripherals that do things.

Type                                                    | Description
-------------                                           | ---------------
[Relay Switch](actuators/relay_switches/README.md)      | Two start state with LED
Buttons  | Action through press
Pumps | Pumping specific qualities of liquid


## Communication Modules
These boards helps communication beween device and peripherals.

Type                                                    | Description
-------------                                           | ---------------
[I2C Multiplexer](communication/i2c_multiplexer/README.md)    | Reduce pins needed
[ADC Module](communication/analog_digital_converter/README.md) | Analog to Digital Converter
