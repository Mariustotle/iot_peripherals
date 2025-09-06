# I²C Interface Overview

The **Inter-Integrated Circuit (I²C)** bus is a communication protocol that allows multiple digital devices to connect using only two wires. It is widely used in microcontrollers, sensors, displays, and other modules due to its simplicity and efficiency.

---

## 1. Core Concepts of I²C
- **Two-wire bus:**
  - **SDA (Serial Data Line):** Transfers the actual data.
  - **SCL (Serial Clock Line):** Provides the timing for data transfer.
- **Master/Slave Architecture:**
  - **Master:** Usually the microcontroller (e.g., Raspberry Pi or Arduino) that initiates communication.
  - **Slaves:** Devices like sensors, ADCs, or LCD controllers that respond when addressed.
- **Device Addressing:**
  - Each I²C device has a **unique 7-bit or 10-bit address.**
  - The master uses this address to select which device to talk to.
- **Speed Modes:**
  - Standard Mode: 100 kbps  
  - Fast Mode: 400 kbps  
  - Fast Mode Plus: 1 Mbps  
  - High-Speed Mode: 3.4 Mbps

---

## 2. Why Use I²C?
- **Fewer Pins:** Only 2 wires are needed regardless of how many devices are connected.
- **Multi-Device Support:** Many devices can share the same bus (SDA/SCL).
- **Simplicity:** Great for simple, short-range communication inside a board or device.
- **Wide Support:** Most sensors, displays, and converters (like ADC/DAC) come with I²C interfaces.

---

## 3. I²C in LCD Displays
Standard character LCDs (16x2, 20x4) normally require multiple parallel pins:
- RS, E, D4–D7, plus power and ground.

With an **I²C backpack (PCF8574 I/O expander):**
- The 8 parallel pins are controlled via I²C.
- Only **VCC, GND, SDA, and SCL** are needed.
- This reduces wiring complexity and frees up GPIO pins on the microcontroller.

---

## 4. Example Devices Using I²C
- **Display Controllers:** PCF8574 backpack for 1602/2004 LCDs.
- **ADC (Analog-to-Digital Converters):** ADS1115, MCP3424.
- **Sensors:** MPU6050 (gyroscope/accelerometer), BME280 (temperature/pressure/humidity).
- **EEPROMs:** 24Cxx series memory chips.

---

## 5. Tradeoffs
- **Pros:**
  - Easy wiring (2 wires for many devices).
  - Standardized protocol with wide support.
  - Good for moderate speed communication.

- **Cons:**
  - Limited cable length (~1–2 meters practical).
  - Shared bus: only one master can talk at a time.
  - Slower than SPI for high-speed applications.

---
