# Temperature Switch Setup


## Overview


## Connection


### Sensor Configuration

Pin functions (HW-503):

- A0 → Analog voltage output from the thermistor divider (to ADC module)
- G → Ground
- + → VCC (3.3–5 V)
- D0 → Digital comparator output (HIGH/LOW depending on threshold)


## Configuration

```json

    "Sensors" : {
            "DigitalTemperatureSensors" :
            [
                {
                    "name": "Server Room Temp",
                    "driver": null,
                    "gpio_pin": 4,
                    "measurement": "Celsius"
                }
            ],
    }

```
