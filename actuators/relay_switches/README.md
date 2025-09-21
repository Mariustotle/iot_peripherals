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
                "driver": null, /* Default driver */
                "default_power_status": null,  /* Default is OFF */
                "gpio_pin": 12, /* GPIO PIN Address */
                "is_low_voltage_trigger": null /* Default is true */               
            },
            {
                "name": "Outside Light",
                "driver": "jqc3f_05vdc_c",
                "default_power_status": "On",
                "pin_position": 12,  /* PIN Position Address */
                "is_low_voltage_trigger": false    
            }
        ]
    }
}
```

## Troubleshooting

### General
- [X] Bypasses all unnecesary cables and devices, smallest working unit first.
- [X] If you connect the GPIO IN to GROUND the Green Light comes on.
- [X] You can switch the Relay on manually through bash commands
  ```bash
  # Set pin LOW
  gpioset gpiochip0 12=0
  raspi-gpio get 12

  # Set pin HIGH
  gpioset gpiochip0 12=1
  raspi-gpio get 12

  gpioinfo
  ```


### The RED light stays on and do not change



