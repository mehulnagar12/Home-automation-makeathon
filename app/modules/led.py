led_stream = None
oldFlag = False

def led_handler(message):
    global oldFlag
    if not oldFlag:
        oldFlag = True
    else:
        print("LED-"+str(message["path"])[1:]+" "+str(message["data"]))

def setStream(db, id):
    led_stream = db.child("Sensor").child("Lighting").stream(led_handler, id, stream_id="led")
