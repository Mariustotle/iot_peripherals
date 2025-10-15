# Common Troubleshooting Playbooks
These are general investigation toolkit.


# I2C Investigations

**Prerequisites**
- Device is connected to the correct pins
  - GPIO3/SCL
  - GPIO2/SDA
  
- I2C is enabled on your Raspberi Pi
  1. Start CLI config ```sudo raspi-config```
  2. Select "Interfacing Options"
  3. Select "I2C"
  4. Enable "Yes"

- Install Libraries if missing
  - ```sudo apt install i2c-tools```

## Is the device I2C working?

```bash
# Show available Busses
ls /dev/i2c*

# Show grid of I2C connected devices
i2cdetect -y 1
```