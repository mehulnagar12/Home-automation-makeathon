import config

def init():
    global oldFlag
    oldFlag = False

def smoke_handler(message):
    global oldFlag
    if not oldFlag:
        oldFlag = True
    else:
        print("Smoke "+str(message["data"]))

def setStream():
    smoke_stream = config.db.child("Sensor").child("Smoke").stream(smoke_handler, config.id, stream_id="smoke")

# To turn it off
def setData(data):
    config.db.child("Sensor").child("Smoke").setValue(data)
