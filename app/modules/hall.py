import config

def init():
    global oldFlag
    oldFlag = False

def hall_handler(message):
    global oldFlag
    if not oldFlag:
        oldFlag = True
    else:
        print("Hall "+str(message["data"]))

def setStream():
    hall_stream = config.db.child("Sensor").child("Security").stream(hall_handler, config.id, stream_id="hall")

# To turn it off
def setData(data):
    config.db.child("Sensor").child("Security").setValue(data)
