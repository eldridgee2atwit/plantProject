import serial
import time

class plantData:
    def __init__(self, port="/dev/ttyUSB1", baudrate=115200, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        try:
            self.ser = serial.Serial(port=self.port, baudrate=self.baudrate, timeout=self.timeout)
            # Clear any stale data in the buffer
            #self.ser.reset_input_buffer()
            #time.sleep(0.1)  # Give the serial port time to stabilize
        except Exception as e:
            self.ser = None
    def _readData(self, index):
            data = (self.ser.read_until(b'\n').decode('utf-8'))
            parts = data.split(',')
            return(parts[index])

    def readLight(self):
        try:
            return(int(self._readData(0)))
        except ValueError:
           return 3000 # error in this part 
    def readMoisture(self):
        try:
            return(int(self._readData(1)))
        except ValueError:
            return 3001 # error in this part 


    # def readLight(self):
    #     if self.ser is None:
    #         return 1  # Default to OFF on error
    #     try:
    #         #self.ser.reset_input_buffer()  # Clear any stale data
    #         value = self.ser.read_until(",").decode('utf-8').strip()
    #         return int(value)
    #     except Exception as e:
    #         print(f"Error reading light: {e}")
    #         return 1  # Default to OFF on error

    # def readMoisture(self):
    #     if self.ser is None:
    #         return 1000  # Error code 1000: No serial connection
    #     try:
    #         #self.ser.reset_input_buffer()  # Clear any stale data
    #         data = str(self.ser.read_until('\n').decode('utf-8')).strip()
    #         parts = data.split(',')
    #         if len(parts) > 1:
    #             return int(parts[1])
    #         return 1001  # Error code 1001: No comma found
    #     except ValueError:
    #         return 1002  # Error code 1002: Could not convert to integer
    #     except Exception as e:
    #         return 1003  # Error code 1003: General error

    def close(self):
        if hasattr(self, 'ser') and self.ser is not None:
            try:
                self.ser.close()
            except:
                pass