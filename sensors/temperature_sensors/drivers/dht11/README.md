# Digital Temperature Sensor Setup

![Digital Temperature Sensor](https://raw.githubusercontent.com/Mariustotle/universal_iot_hub/refs/heads/main/resources/sensors/digital_temperature_sensor/DHT11_blue.png)

## Overview


## Connection


### Sensor Configuration

Pin functions (DHT11):

- S - Signal / Data
- VCC - 5V Power
- [-] - Ground


## Configuration

```json
{
    "Peripherals": [
        {
            "type": "DigitalTemperatureSensor",
            "name": "Server Room Temperature",
            "driver": "dht11",
            "gpio_pin": 26,
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