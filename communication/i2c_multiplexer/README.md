# I²C Interface Overview

The **Inter-Integrated Circuit (I²C)** bus is a communication protocol that allows multiple digital devices to connect using only two wires. It is widely used in microcontrollers, sensors, displays, and other modules due to its simplicity and efficiency. [Read More](explainer.md)

## Configuration
The configuration is built up from the I2C config and where it is referenced in other peripherals.

```json

    "CommunicationModules": {
        "I2CExpanders": 
        [
            {
                "name": "I2C for LCD",
                "multiplexer_address": "0x76",
                "number_of_channels": 8
            }
        ]
    }

```
