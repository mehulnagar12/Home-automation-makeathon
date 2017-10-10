hall_stream = None
oldFlag = False

def hall_handler(message):
    global oldFlag
    if not oldFlag:
        oldFlag = True
    else:
        print("Hall "+str(message["data"]))

def setStream(db, id):
    hall_stream = db.child("Sensor").child("Security").stream(hall_handler, id, stream_id="hall")

# To turn it off
def setData(db, data):
    db.child("Sensor").child("Security").setValue(data)
