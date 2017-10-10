temp_stream = None
oldFlag = False

def temp_handler(message):
    global oldFlag
    if not oldFlag:
        oldFlag = True
    else:
        print("Temperature "+str(message["data"]))

def setStream(db, id):
    temp_stream = db.child("Sensor").child("Temperature").stream(temp_handler, id, stream_id="temp")
