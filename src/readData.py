import serial

try:
    ser = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)
    print("Successfully connected to serial port")
except Exception as e:
    print(f"Failed to connect to serial port: {e}")
    ser = None

def read_light():
    if ser is None:
        print("No serial connection, returning test value")
        return 75  # Test value
    try:
        received_data = ser.read_until('\n').decode('utf-8')
        print(f"Received light data: {received_data}")
        return int(received_data)
    except Exception as e:
        print(f"Error reading light: {e}")
        return 75  # Test value

def read_moisture():
    if ser is None:
        print("No serial connection, returning test value")
        return 60  # Test value
    try:
        received_data = ser.read_until('\n').decode('utf-8')
        print(f"Received moisture data: {received_data}")
        return int(received_data)
    except Exception as e:
        print(f"Error reading moisture: {e}")
        return 60  # Test value
