# Digital Temperature Sensor Setup

![Digital Temperature Sensor](https://raw.githubusercontent.com/Mariustotle/universal_iot_hub/refs/heads/main/resources/sensors/digital_temperature_sensor/DHT11_blue.png)

## Overview


## Connection


### Sensor Configuration

Pin functions (AHT10):

- VIN - 3.3v Power
- GND - Ground
- SCL - I2C SCL
- SDA - I2C SDA

## Configuration

```json
{
    "Peripherals": [
        /* Example of configuration using I2C on the main board */
        {
            "type": "DigitalI2CTemperatureSensor",
            "name": "Outside Braai Area Temperature",
            "channel": 1,
            "driver": "aht10",
            "gpio_pin_sda": 2,
            "gpio_pin_scl": 3,
            "measurement": "Celsius"
        }
    ]
}
```


## Troubleshooting

If you have trouble installing the PIP package
```bash

# Open you project folder in bash
cd projects/universal_iot_hub/

# Start your virual environment
source local_env/bin/activate

# Open the parent folder
cd ..

# Download the source code
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT

# Install but specify this is a raspbery pi OS
python setup.py install --force-pi

# View that install was successfull
pip list

```