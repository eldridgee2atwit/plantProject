import serial

try:
    ser = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)
except:
    ser = None

def read_light():
    if ser is None:
        return 75  # Test value
    try:
        received_data = ser.read_until('\n').decode('utf-8')
        return int(received_data)
    except:
        return 75  # Test value

def read_moisture():
    if ser is None:
        return 60  # Test value
    try:
        received_data = ser.read_until('\n').decode('utf-8')
        return int(received_data)
    except:
        return 60  # Test value
