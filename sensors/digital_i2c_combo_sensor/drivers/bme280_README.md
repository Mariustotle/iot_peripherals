# Digital Temperature Sensor Setup

![Digital Temperature Sensor](https://raw.githubusercontent.com/Mariustotle/universal_iot_hub/refs/heads/main/resources/sensors/digital_temperature_sensor/tenstar_bme280.png)

## Overview


## Hardware Configuration

The Tenstar BME280 breakout has the following pins:

- VIN → 3.3V (⚠️ use 3.3V, not 5V, as the sensor is not 5V tolerant)
- GND → Ground
- SCL → Raspberry Pi GPIO3 (pin 5) → I²C SCL
- SDA → Raspberry Pi GPIO2 (pin 3) → I²C SDA


## Software Configuration

### Special Libraries
```bash
# Ensure you are in the local python instance (busio / board)
python -m pip install adafruit-blinka
```


Make sure:
I²C is enabled on your Raspberry Pi (In Bash)




```bash
# Open the config
sudo raspi-config
```

1. Select "Interfacing Options"
2. Select "I2C"
3. Enable "Yes"

```bash
# Check if I2C is working
sudo i2cdetect -y 1
```


(raspi-config → Interface Options → enable I²C).

You have installed smbus2 or adafruit-circuitpython-bme280 as the driver backend.


## Configuration File

```json

    "Sensors" : {
        "I2CComboSensors" :
        [
            {
                "name": "Workshop ENV Sensor",
                "driver": null,
                "i2c_address": "0x76",
                "measurement": "Celsius"
            }
        ],
    }

```


## Troubleshooting

Default I2C Address is 0x76 (Sometimes 0x77 if pulled high), if your sensor does not show up run the below to see the address:

```bash
# Shows any connected I2C devices, dashes if nothing is detected
sudo i2cdetect -y 1
```