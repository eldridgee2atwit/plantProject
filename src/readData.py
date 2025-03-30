import serial
ser = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)
try:
    while ser.is_open:
        received_data = ser.read_until('\n').decode('utf-8')
        print(received_data)
except KeyboardInterrupt:
    ser.close()
