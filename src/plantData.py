import serial
import time

class plantData:
    def __init__(self, port="/dev/ttyUSB0", baudrate=115200, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        try:
            self.ser = serial.Serial(port=self.port, baudrate=self.baudrate, timeout=self.timeout)
            # Clear any stale data in the buffer
            self.ser.reset_input_buffer()
            time.sleep(0.1)  # Give the serial port time to stabilize
        except Exception as e:
            print(f"Failed to initialize serial port: {e}")
            self.ser = None

    def readLight(self):
        if self.ser is None:
            return "1"  # Default to OFF on error
        try:
            self.ser.reset_input_buffer()  # Clear any stale data
            value = self.ser.read_until(",").decode('utf-8').strip()
            return value
        except Exception as e:
            print(f"Error reading light: {e}")
            return "1"  # Default to OFF on error

    def readMoisture(self):
        if self.ser is None:
            return 1000
        try:
            self.ser.reset_input_buffer()  # Clear any stale data
            data = str(self.ser.read_until('\n').decode('utf-8')).strip()
            index = data.find(',')
            if index == -1:
                print("No comma found in moisture data")
                return 1000
            return int(data[index+1])
        except Exception as e:
            print(f"Error reading moisture: {e}")
            return 1000

    def close(self):
        if hasattr(self, 'ser') and self.ser is not None:
            try:
                self.ser.close()
            except:
                pass