# TDS Sensor


## Overview


## Connection


### Sensor Configuration

Pin functions:

- S - Signal / Data
- VCC - 5V Power
- [-] - Ground


## Configuration

```json
{
    "Peripherals": [
        {
            "type": "DigitalTemperatureSensor",
            "name": "Water Particle Meter",
            "driver": null,
            "number_of_readings": 5,
            "delay_between_readings": 0.3,
            "gpio_pin": 12
        }
    ]
}
```


