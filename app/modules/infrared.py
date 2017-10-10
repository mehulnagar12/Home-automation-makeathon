import config

def init():
    global oldFlag
    oldFlag = False

def infra_handler(message):
    global oldFlag
    if not oldFlag:
        oldFlag = True
    else:
        print("AC "+str(message["data"]))

def setStream():
    infra_stream = config.db.child("Sensor").child("AC").stream(infra_handler, config.id, stream_id="ac")

def setValue(data):
    config.db.child("Sensor").child("AC").push(data, config.id)
