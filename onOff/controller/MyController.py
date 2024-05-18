#!C:\Python\python.exe

import serial
import cgi
import sys
import time

print("Content-Type: text/plain\n")

ser = serial.Serial('COM5', 9600)
time.sleep(2)  # Wait for the connection to initialize

# Get data from the form
form = cgi.FieldStorage()
action = form.getvalue('action')

# Send the appropriate command to the Arduino
if action == 'on':
    ser.write(b'N')
    status = "Pin 2 turned ON"
elif action == 'off':
    ser.write(b'F')
    status = "Pin 2 turned OFF"
else:
    status = "Unknown action"

# Close the serial connection
ser.close()

# Send a response back to the web browser
print(status)
