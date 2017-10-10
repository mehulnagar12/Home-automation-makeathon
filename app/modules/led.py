# Controller for LEDs
import serial

def getLEDs():
    return serial.read()["led"]

def setLEDs(data): #LED data is in the form {1: 0/1, ... 5: 0/1 }
    print("write")
