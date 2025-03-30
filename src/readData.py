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
        light, _ = read_serial_data()
        if light is None:
            return 0
        return 1 if light > 0 else 0
    except:
        return 0

def read_moisture():
    if ser is None:
        return 1000
    try:
        _, moisture = read_serial_data()
        if moisture is None:
            return 1000
        return moisture
    except:
        return 1000
