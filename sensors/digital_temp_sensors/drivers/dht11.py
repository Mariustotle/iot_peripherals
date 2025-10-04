from peripherals.contracts.temperature_measurement import TemperatureMeasurement
from peripherals.sensors.digital_temp_sensors.driver_base import DigitalTempDriverBase
from peripherals.sensors.digital_temp_sensors.response import DigitalTempResponse

import RPi.GPIO as GPIO
import time


class DHT11(DigitalTempDriverBase):

    def initialize(self) -> bool:

        try:
            GPIO.setmode(GPIO.BCM)
            return True

        except Exception as ex:
            print(f"Oops! {ex.__class__} Unable to intialize [{self.driver_name}]. Details: {ex}")

        return False
    
    def _collect_input(self, pin):
        count = []
        last = -1
        current_len = 0

        # Record change in pin state
        for i in range(10000):  # safety stop
            current = GPIO.input(pin)
            if current != last:
                count.append(current_len)
                current_len = 1
                last = current
            else:
                current_len += 1

        return count

    def _parse_data(self, count):
        data = count[4:]  # skip initial transitions
        bits = []

        for i in range(0, len(data), 2):
            if i + 1 >= len(data):
                break
            low = data[i]
            high = data[i + 1]
            bit = 1 if high > low else 0
            bits.append(bit)

        if len(bits) < 40:
            print(f"[DEBUG] Incomplete bitstream ({len(bits)} bits):", bits)
            return None

        print(f"[DEBUG] Raw bits: {bits[:40]}")
        return bits[:40]
    
    
    def read_raw(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        # Send start signal
        GPIO.output(pin, GPIO.LOW)
        time.sleep(0.02)  # 20ms
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.00004)  # 40us
        GPIO.setup(pin, GPIO.IN)

        # Wait for response
        count = self._collect_input(pin)

        # Parse bits from timing
        bits = self._parse_data(count)

        if bits is None or len(bits) != 40:
            raise Exception(f"Invalid reading. bits = [{str(bits)}]")

        # Convert to bytes
        data = []
        for i in range(0, 40, 8):
            byte = 0
            for j in range(8):
                byte = (byte << 1) | bits[i + j]
            data.append(byte)

        checksum = sum(data[:4]) & 0xFF
        if data[4] != checksum:
            raise Exception(f"Checksum error. [{str(data[4])}] != [{str(checksum)}]")

        humidity = data[0]
        temperature = data[2]
        return temperature, humidity


    def _default_reading(self) -> float:
        (humidity, temperature) = self.read_raw(self.gpio_pin)

        if temperature is not None:
            if self.config.measurement == TemperatureMeasurement.Fahrenheit:
                temperature = (temperature * 9/5) + 32

        return DigitalTempResponse.create(
            temperature=temperature,
            measurement=self.config.measurement,
            humidity=humidity
        )    


    def cleanup(self):
        GPIO.cleanup()