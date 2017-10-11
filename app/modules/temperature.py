import config

def init():
    global oldFlag
    oldFlag = False

def temp_handler(message):
    global oldFlag
    if not oldFlag:
        oldFlag = True
    else:
        print("Temperature "+str(message["data"]))

def setStream():
    temp_stream = config.db.child("Sensor").child("Temperature").stream(temp_handler, config.id, stream_id="temp")

def setValue(value):
    config.db.child("Sensor").child("Temperature").set(value, config.id)
