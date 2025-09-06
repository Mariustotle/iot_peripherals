# Analog to Digital Converter (ADC) Setup

An **Analog to Digital Converter (ADC)** takes a continuous analog signal (like a voltage from a sensor) and converts it into a discrete digital value your microcontroller or Raspberry Pi can read.

---

## 1. Core Concepts of ADC
- **Resolution (bits):** How finely the ADC can divide the input range.  
  - Example: 10-bit ADC = 2¹⁰ = 1024 levels. With a 0–5V input, each step is ~4.9 mV.
- **Reference Voltage (Vref):** Maximum voltage the ADC can measure. Can be internal (1.1V, 2.5V, etc.) or external.
- **Sampling Rate:** How many times per second the ADC takes a measurement. High-speed is needed for audio, low-speed is fine for temperature.
- **Input Type:**  
  - **Single-ended:** Voltage relative to ground.  
  - **Differential:** Voltage difference between two pins.

---

## 2. ADC Configurations
Different chips and microcontrollers let you set ADCs up in a few ways:

### a. Single-Ended Mode
- One channel measures voltage relative to ground.
- Example: measuring a sensor output that swings 0–5V.

### b. Differential Mode
- Measures the voltage difference between two inputs.
- Useful for small signals in noisy environments (e.g., ±50 mV amplified against 5V).

### c. Pseudo-Differential
- One input is referenced against a fixed internal/common pin instead of true ground.
- Less accurate than full differential, but cheaper.

### d. Continuous vs. Single-Shot
- **Continuous mode:** ADC keeps sampling automatically.  
- **Single-shot mode:** ADC only samples when triggered, saving power.

### e. Internal vs. External Reference
- **Internal:** Microcontroller has a fixed Vref (like 3.3V).  
- **External:** You supply a precise reference voltage pin for higher accuracy.

---

## 3. ADC Channels
Most ADCs are **multiplexed**:
- A single ADC core with a multiplexer (MUX) that switches between multiple inputs.
- Example: A 4-channel ADC can read 4 different sensors, but only one at a time.
- Switching is very fast, so it feels like "parallel" sampling.

### Channel Options
- **Single Channel:** Only one input (common in cheap ADC chips).  
- **Multi-Channel (MUX):** Lets you select among several inputs (like ADS1115 with 4 channels).  
- **Simultaneous Sampling:** Some advanced ADCs have multiple ADC cores so they can read all channels at the same exact instant (important for things like audio or 3-phase current measurement).

---

## 4. Practical Example: ADS1115
The ADS1115 is popular in Raspberry Pi/Arduino projects:
- **16-bit resolution** (65,536 steps).  
- **4 channels total.**  
- Configurable as:  
  - 4 single-ended channels  
  - 2 differential pairs  
- **Programmable gain amplifier** built-in (to scale small signals before converting).  
- **I²C interface**, so you just connect SDA/SCL and read digital values.

---

## 5. Tradeoffs
- **More resolution** → slower conversions (usually).  
- **More channels** → more switching overhead.  
- **Higher sampling rate** → more noise, lower accuracy.  
- **Single-ended** → simpler, but more prone to noise.  
- **Differential** → more robust, but halves your channel count.

---
