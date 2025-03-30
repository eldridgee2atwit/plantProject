import serial
import time

try:
    ser = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)
except:
    ser = None

def read_serial_data():
    if ser is None:
        return None
    try:
        ser.reset_input_buffer()
        time.sleep(0.1)
        data = ser.read_until('\n').decode('utf-8')
        return data.strip('\r\n').split(',')[0]
    except:
        return None

def read_light():
    if ser is None:
        return 0
    try:
        value = read_serial_data()
        if value is None:
            return 0
        return 1 if int(value) > 0 else 0
    except:
        return 0

def read_moisture():
    if ser is None:
        return 1000
    try:
        value = read_serial_data()
        if value is None:
            return 1000
        return int(value)
    except:
        return 1000
