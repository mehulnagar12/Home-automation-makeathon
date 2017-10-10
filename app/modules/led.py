import config

def init():
    global oldFlag
    oldFlag = False

def led_handler(message):
    global oldFlag
    if not oldFlag:
        oldFlag = True
    else:
        print("LED-"+str(message["path"])[1:]+" "+str(message["data"]))

def setStream():
    led_stream = config.db.child("Sensor").child("Lighting").stream(led_handler, config.id, stream_id="led")

def setLED(number, value):
    try:
        config.db.child("Sensor").child("Lighting").child(number).set(value, config.id)
    except Exception as e:
        print("Database error")
        print(e)
