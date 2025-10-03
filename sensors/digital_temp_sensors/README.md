# Digital Temperature Sensor Setup

![Digital Temperature Sensor](https://raw.githubusercontent.com/Mariustotle/universal_iot_hub/refs/heads/main/resources/sensors/digital_temperature_sensor/DHT22.png)

## Overview


## Connection


### Sensor Configuration

Pin functions (DHT11):

- S - Signal / Data
- VCC - 5V Power
- [-] - Ground


## Configuration

```json

    "Sensors" : {
        "DigitalTemperatureSensors" :
        [
            {
                "name": "Server Room Temperature",
                "driver": null,
                "gpio_pin": 12,
                "measurement": "Celsius"
            }
        ],
    }

```
