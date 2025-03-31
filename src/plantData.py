import serial
import threading
import queue

class plantData:
    def __init__(self, port="/dev/ttyUSB0", baudrate=115200, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.q = queue.Queue()
        self.data = ("1","1")
        self.running = True
        try:
            self.ser = serial.Serial(port=self.port, baudrate=self.baudrate, timeout=self.timeout)
            read_thread = threading.Thread(target=self._readData)
            read_thread.daemon = True
            read_thread.start()
        except Exception as e:
            self.ser = None

    def _readData(self):
        while self.running:
            if self.ser is None:
                return
            try:
                raw_data = self.ser.read_until(b'\n').decode('utf-8').strip()
                self.data = tuple(raw_data.split(','))
            except Exception as e:
                print(f"Error reading from serial: {e}")
    
        # if self.ser is None:
        #     return "1"  # Default to OFF on error
        # try:
        #     self.ser.reset_input_buffer()  # Clear any stale data
        #     value = self.ser.read_until(",").decode('utf-8').strip()
        #     return value
        # except Exception as e:
        #     print(f"Error reading light: {e}")
        #     return "1"  # Default to OFF on error

    def getData(self):
        return self.data
        # if self.ser is None:
        #     return 1000  # Error code 1000: No serial connection
        # try:
        #     self.ser.reset_input_buffer()  # Clear any stale data
        #     data = str(self.ser.read_until('\n').decode('utf-8')).strip()
        #     parts = data.split(',')
        #     if len(parts) > 1:
        #         return int(parts[1])
        #     return 1001  # Error code 1001: No comma found
        # except ValueError:
        #     return 1002  # Error code 1002: Could not convert to integer
        # except Exception as e:
        #     return 1003  # Error code 1003: General error

    def close(self):
        if hasattr(self, 'ser') and self.ser is not None:
            try:
                self.ser.close()
            except:
                pass