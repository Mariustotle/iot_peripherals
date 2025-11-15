# Relay Setup
A relay module is an electrically operated switch that allows a low-power device (like a Raspberry Pi or Arduino) to control a high-power circuit (such as lamps, motors, or appliances).

![Relay Module Picture](https://raw.githubusercontent.com/Mariustotle/universal_iot_hub/refs/heads/main/resources/actuators/relay_module/relay_module.png)

## Overview

### Requirement
- A Relay Module with LED's (Red = Powered, Green = Activated) - Without them it is difficult to see state.
- A "Low Level Trigger", this will invert the LOW/HIGH so that a LOW GPIO voltage will activate the relay. Without this you will need additional hardware as Raspberry Pi's GPIO pins (not the power pins) only go to 3.3V so cannot reach the 5V HIGH to activate.


### Input side (low-voltage control)

- VCC → 5V power supply
- GND → Ground
- IN → Control signal from GPIO

### Output side (high-voltage switch)

- COM (Common)
- NO (Normally Open) → default is disconnected, closes when relay is ON
- NC (Normally Closed) → default is connected, opens when relay is ON

### Indicators
- Red LED → Power indicator (always on when VCC is supplied)
- Green LED → Relay status (on when GPIO drives relay active)

⚠️ Warning: While the control side is safe (5V logic), the relay can switch dangerous mains voltage. Extreme caution is required when connecting AC devices.

## Connection

1. Board Power: Connect VCC → 5V and GND → GND on the Raspberry Pi.
2. Signal Pin: Connect IN → GPIO (e.g., GPIO12).   


### Triggering Mechanisms
If you do not have a 3.3V Relay Module (Not common e.g. V-logic relay/ULN2003) and you do not have a "Low Level Trigger" then you will need to bridge the gap between the Pi and the Relay Module. Here are some options:

- Add a NPN Transistor, e.g. 2N2222 (switch) with a 1kΩ Resistor (Protect lower voltage Pi GPIO connection).
  - Relay Power
    - VCC → Pi 5 V pin
    - GND → Pi GND pin (must be common with emitter!)
  - Transistor
    - Emitter (E) → Pi GND
    - Collector (C) → Relay IN pin
    - Base (B) → Pi GPIO (e.g. BCM18) via 1 kΩ resistor
  - Pull-up Resistor
    - Add a 10 kΩ resistor from relay IN → relay VCC (5 V).
    - Ensures IN is HIGH (relay OFF) whenever transistor isn’t pulling low.
  
- Use a level shifter
  - A logic-level MOSFET or a proper level-shifting IC (e.g., 74HC245, ULN2003 driver, etc.) can translate the Pi’s 3.3 V logic to proper 5 V drive for the relay board.



## ⚙️ Configuration

Setting                         | Description
-------------                   | ---------------
Default Power Status            | Relay switches allow for either ON or OFF at rest power conection i.e., a default ON power connection will require you to trigger the relay to switch it off and vice versa.
Is Low Voltage Trigger          | Inverts the HIGH/LOW trigger so that by default LOW is the trigger and HIGH is the resting position.
Use Direction Control           | When you have a "Low Voltage Trigger" then you can use the INPUT/OUTPUT with the default ON (Always have a low voltage) to trigger without the need of a 5V GPIO source


```json
{
  "Peripherals": [
    {
        "type": "RelaySwitch",
        "name": "Bedroom Light",
        "driver": "jqc3f_05vdc_c",
        "default_power_status": "Off",
        "gpio_pin": 13,
        "is_low_voltage_trigger": true,
        "use_direction_control": true
    }
  ]
}
```

## Troubleshooting

### General
- [X] Most simple version to start with
  - Bypass all unnecesary cables and devices, smallest working unit first.
- [X] Is your wiring corrent?
  - If you connect the GPIO IN to GROUND the Green Light comes on
- [X] Is the GPIO state changes as expected
  - You can switch the Relay on manually through bash commands
    ```bash
    # Set pin LOW
    gpioset gpiochip0 12=0
    raspi-gpio get 12

    # Set pin HIGH
    gpioset gpiochip0 12=1
    raspi-gpio get 12

    gpioinfo
    ```

