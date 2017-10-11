import config
import controller.serial_controller as serial_controller
import time

def init():
    global oldFlag
    oldFlag = False

def led_handler(message):
    global oldFlag
    if not oldFlag:
        oldFlag = True
    else:
        print("LED-"+str(message["path"])[1:]+" "+str(message["data"]))
        serial_controller.setLED((message["path"])[1:],message["data"])

def setStream():
    led_stream = config.db.child("Sensor").child("Lighting").stream(led_handler, config.id, stream_id="led")

def setLED(number, value):
    try:
        serial_controller.setLED(number, value)
        config.db.child("Sensor").child("Lighting").child(number).set(value, config.id)
        time.sleep(0.5)
    except Exception as e:
        print("Database error")
        print(e)
