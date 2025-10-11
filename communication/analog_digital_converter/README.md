# Analog to Digital Converter (ADC) Setup

An **Analog to Digital Converter (ADC)** takes a continuous analog signal (like a voltage from a sensor) and converts it into a discrete digital value your microcontroller or Raspberry Pi can read. [Read More](explainer.md)


## Configuration
The configuration is built up from the ADC config and where it is referenced in other peripherals.

```json

    "CommunicationModules": {
        "AnalogDigitalConverters": 
        [
            {
                "name": "ADC for TDS",
                "gpio_pin": 18
            }
        ]
    }

```