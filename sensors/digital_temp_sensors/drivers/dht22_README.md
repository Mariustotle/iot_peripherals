# Digital Temperature Sensor Setup

![Digital Temperature Sensor](https://raw.githubusercontent.com/Mariustotle/universal_iot_hub/refs/heads/main/resources/sensors/digital_temperature_sensor/DHT22_white.png)

## Overview


## Connection


### Sensor Configuration

Pin functions (DHT11):

- [+] - 3.3V Power
- OUT - GPIO Data Pin
- [-] - Ground


### Special Libraries

```bash
sudo apt-get install libgpiod2
pip install adafruit-circuitpython-dht
pip install adafruit-blinka
```

## Configuration

```json

    "Sensors" : {
        "DigitalTemperatureSensors" :
        [
            {
                "name": "Server Room Temperature",
                "driver": "dht22",
                "gpio_pin": 12,
                "measurement": "Celsius"
            }
        ],
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