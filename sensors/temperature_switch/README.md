# Temperature Switch Setup

![Temperature Switch](https://raw.githubusercontent.com/Mariustotle/universal_iot_hub/refs/heads/main/resources/sensors/temperature_switch/HW-503_LM393.png)


# Overview


## Connection


### Sensor Configuration




## Configuration

```json

    "Sensors" : {
        "DigitalTemperatureSensors" :
        [
            {
                "name": "Office Temp and Humidity",
                "driver": null,
                "gpio_pin": 18,
                "measurement": "Celsius"
            }
        ],
    }

```
