# Relay Setup
A relay module is an electrically operated switch that allows a low-power device (like a Raspberry Pi or Arduino) to control a high-power circuit (such as lamps, motors, or appliances).


## Overview

### Requirement
For Raspberry Pi you need a Relay Module that is "Low Level Trigger", this will allow the 3.3V GPIO data pin to set ON/OFF. You can use the 5V but then you will need to include some hardware to bridge the gap, note the relay is powered by a 5V but this is talking about the GPIO power which on a Raspberry Pi is 3.3V (Higher voltage here will hurt the Pi). See the troublehooting section for more details.

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
- Red LED → Relay status (on when GPIO drives relay active)

⚠️ Warning: While the control side is safe (5V logic), the relay can switch dangerous mains voltage. Extreme caution is required when connecting AC devices.

## Connection

1. Board Power: Connect VCC → 5V and GND → GND on the Raspberry Pi.
2. Signal Pin: Connect IN → GPIO (e.g., GPIO17 / Pin 11).   


### Default Behavior
These modules are usually active LOW i.e., That means:
- GPIO LOW (0V) → Relay ON (red LED on, NO closes to COM).
- GPIO HIGH (3.3V) → Relay OFF (red LED off, NO open).

## ⚙️ Configuration

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

## Troubleshooting

### General
- Start simple, connect the Relay directly to the Raspberry PI and run the most simple version of the code. I.E. remove all non-essential components until you have a successfull test.


### The RED light stays on and do not change
After doing the basic testing above, check if you have a 5V Relay Module. Short your IN to Ground (Give it 5V) if the green light comes up then you have a 5V Relay Module so will need to add some hardware.

You have a couple of options
- Add a NPN (Negative-Positive-Negative) transister + resistor and use the 5V power
  Example resister: 2N2222
- Relay Power
  - VCC → Pi 5 V pin
  - GND → Pi GND pin (must be common with emitter!)
- Transistor (Flat face to you: [E]-[C]-[B])
  - Emitter (E) → Pi GND
  - Collector (C) → Relay IN pin
  - Base (B) → Pi GPIO (e.g. BCM18) via 1 kΩ resistor
- Pull-up Resistor
  - Add a 10 kΩ resistor from relay IN → relay VCC (5 V).
  - Ensures IN is HIGH (relay OFF) whenever transistor isn’t pulling low.
  
- ULN2003/ULN2803 driver board (Simular to NPN but for up to 8 channels)


