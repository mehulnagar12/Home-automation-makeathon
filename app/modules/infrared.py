infra_stream = None
oldFlag = False

def infra_handler(message):
    global oldFlag
    if not oldFlag:
        oldFlag = True
    else:
        print("AC "+str(message["data"]))

def setStream(db, id):
    infra_stream = db.child("Sensor").child("AC").stream(infra_handler, id, stream_id="ac")
