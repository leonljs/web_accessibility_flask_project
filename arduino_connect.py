import serial
import time
arduino = serial.Serial('/dev/cu.usbserial-14310', timeout=5)
encoding = 'utf-8'
while True:
    data = arduino.readline()
    data = str(data, encoding)
    print(data)
