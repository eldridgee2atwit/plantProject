import serial
import time

try:
    ser = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)
except:
    ser = None

def read_serial_data():
    if ser is None:
        return None, None
    try:
        ser.reset_input_buffer()
        time.sleep(0.1)
        data = ser.read_until('\n').decode('utf-8').strip('\r\n')
        parts = data.split(',')
        if len(parts) == 2:
            return int(parts[0]), int(parts[1])
        return None, None
    except:
        return None, None

def read_light():
    if ser is None:
        return 0
    try:
        value = ser.read_until(",").decode('utf-8')
        return 1 if int(value) > 0 else 0
    except:
        return 0

def read_moisture():
    if ser is None:
        return 1000
    try:
        data = str(ser.read_until('\n').decode('utf-8'))
        index = data.find(',')
        return int(data[index+1])
    except:
        return 1000
