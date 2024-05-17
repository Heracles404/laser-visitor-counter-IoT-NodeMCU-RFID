#!C:\Python\python.exe

print("Content-Type: text/html")
print()
import serial
import cgi

form = cgi.FieldStorage()
action = form.getvalue("action")

ser = serial.Serial('COM12', 9600)

if action == "ON":
    state = b'N'
elif action == "OFF":
    state = b'F'

ser.write(state)
    