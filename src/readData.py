import serial
import time

try:
    ser = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)
    print("Successfully connected to serial port")
except Exception as e:
    print(f"Failed to connect to serial port: {e}")
    ser = None

def parse_serial_data(data):
    # Clean up the data string
    data = data.strip('\r\n')
    # Split by comma and take the first number
    parts = data.split(',')
    if len(parts) > 0:
        try:
            return int(parts[0])
        except:
            return 75  # Default value if parsing fails
    return 75  # Default value if no parts

def read_serial_data():
    if ser is None:
        return None
    try:
        # Clear any existing data in the buffer
        ser.reset_input_buffer()
        # Wait a bit for new data
        time.sleep(0.1)
        received_data = ser.read_until('\n').decode('utf-8')
        return received_data
    except Exception as e:
        print(f"Error reading serial data: {e}")
        return None

def read_light():
    if ser is None:
        print("No serial connection, returning test value")
        return 0  # Default to 0 (off)
    try:
        received_data = read_serial_data()
        if received_data is None:
            return 0
        print(f"Received light data: {received_data}")
        value = parse_serial_data(received_data)
        # Convert to boolean (0 or 1)
        return 1 if value > 0 else 0
    except Exception as e:
        print(f"Error reading light: {e}")
        return 0  # Default to 0 (off)

def read_moisture():
    if ser is None:
        print("No serial connection, returning test value")
        return 60  # Test value
    try:
        received_data = read_serial_data()
        if received_data is None:
            return 60
        print(f"Received moisture data: {received_data}")
        return parse_serial_data(received_data)
    except Exception as e:
        print(f"Error reading moisture: {e}")
        return 60  # Test value
