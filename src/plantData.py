import serial

class plantData() :
    def __init__(self, port="/dev/ttyUSB0", baudrate=115200, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout=timeout
        self.ser = serial.Serial(port=self.port, baudrate=self.baudrate, timeout=self.timeout)

    def readLight(self):
        return self.ser.read_until(",").decode('utf-8')
    def readMoisture(self):
        data = str(self.ser.read_until('\n').decode('utf-8'))
        index = data.find(',')
        return int(data[index+1])