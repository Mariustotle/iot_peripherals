# Digital Temperature Sensor Setup

![Digital Temperature Sensor](https://raw.githubusercontent.com/Mariustotle/universal_iot_hub/refs/heads/main/resources/sensors/digital_temperature_sensor/tenstar_bme280.png)

## Overview


## Hardware Configuration

The Tenstar BME280 breakout has the following pins:

- VIN → 3.3V (⚠️ use 3.3V, not 5V, as the sensor is not 5V tolerant)
- GND → Ground
- SCL → Raspberry Pi GPIO3 (pin 5) → I²C SCL
- SDA → Raspberry Pi GPIO2 (pin 3) → I²C SDA


## Software Configuration

### Special Libraries
```bash
# Ensure you are in the local python instance (busio / board)
python -m pip install adafruit-blinka
python -m pip install adafruit-circuitpython-bme280
```



## Configuration File

```json

    /* Example where built in I2C is used */
    "Sensors" : {
        "I2CComboSensors" :
        [
            {
                "name": "Workshop ENV Sensor",
                "driver": null,                
                "measurement": "Celsius",
                "i2c_address": "0x76",
                "multiplexer": null
            }
        ],
    }

    /* Example where I2C Multiplexer is used, note you need to register a Multiplexer with the same name. */
    "Sensors" : {
        "I2CComboSensors" :
        [
            {
                "name": "Workshop ENV Sensor",
                "driver": null,                
                "measurement": "Celsius",
                "i2c_address": "0x76",
                "multiplexer_details": {
                    "name": "I2C Extender",
                    "channel": 1
                }
            }
        ],
    }

```


## Troubleshooting

- [I2C Troubleshooting](../../../troubleshooting.md)