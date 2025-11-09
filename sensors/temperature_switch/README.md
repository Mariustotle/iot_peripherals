# Temperature Switch Setup

![Temperature Switch](https://raw.githubusercontent.com/Mariustotle/universal_iot_hub/refs/heads/main/resources/sensors/temperature_switch/HW-503_LM393.png)


# Overview


## Connection


### Sensor Configuration

- A0 → Analog voltage output from the thermistor divider (to ADC module)
- G → Ground
- [+] → VCC (3.3–5 V)
- D0 → Digital comparator output (HIGH/LOW depending on threshold)


## Configuration

```json

    "Sensors" : {
        "TemperatureSwitches" :
            [
                {
                    "name": "Office Temp and Humidity",
                    "driver": null,
                    "gpio_out_pin": 16,
                    "switch_threshold": 25.0,
                    "measurement": "Celsius"
                }
            ],
    }

```
