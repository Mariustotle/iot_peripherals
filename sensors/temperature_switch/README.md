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
        "TemperatureSwitches" :
        [
            {
                "name": "Server Room Temperature",
                "adc_module": "module a",
                "driver": null,
                "gpio_out_pin": 4,
                "switch_threshold": 12.3,
                "measurement": "Celsius"
            }
        ],
    }

```
