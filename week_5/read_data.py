import serial
import time
import ujson

ser = serial.Serial('COM34', 115200)  # Make sure to use the correct COM port

while True:
    line = ser.readline().decode('utf-8').rstrip()
    print("Received data:", line)
    time.sleep(1)  # Adjust the delay based on your needs
