import serial
import time

print("Check!")

ser = serial.Serial('COM10', 9600)

while True:
    user_input = input("Enter Control: ")
    if user_input.upper() == 'ON':
        ser.write(b'1')
    elif user_input.upper() == 'OFF':
        ser.write(b'2')  
    else:
            print("Invalid input.")
