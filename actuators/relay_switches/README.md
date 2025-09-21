# Relay Setup
A relay module is an electrically operated switch that allows a low-power device (like a Raspberry Pi or Arduino) to control a high-power circuit (such as lamps, motors, or appliances).




## Overview

### Input side (low-voltage control)

- VCC → 5V power supply
- GND → Ground
- IN → Control signal from GPIO

### Output side (high-voltage switch)

- COM (Common)
- NO (Normally Open) → default is disconnected, closes when relay is ON
- NC (Normally Closed) → default is connected, opens when relay is ON

### Indicators
- Green LED → Power indicator (always on when VCC is supplied)

Red LED → Relay status (on when GPIO drives relay active)

⚠️ Warning: While the control side is safe (5V logic), the relay can switch dangerous mains voltage. Extreme caution is required when connecting AC devices.

## ⚙️ Connection

1. Board Power: Connect VCC → 5V and GND → GND on the Raspberry Pi.
2. Signal Pin: Connect IN → GPIO (e.g., GPIO17 / Pin 11).   


### Default Behavior
These modules are usually active LOW i.e., That means:
- GPIO LOW (0V) → Relay ON (red LED on, NO closes to COM).
- GPIO HIGH (3.3V) → Relay OFF (red LED off, NO open).

## Configuration

```json
{
    "Actuators" : {
        "RelaySwitches" : 
        [
            {
                "name": "Bedroom Light",
                "driver": "jqc3f_05vdc_c",
                "default_status": "Off",
                "gpio_pin": 18                           
            }
        ]
    }
}
```