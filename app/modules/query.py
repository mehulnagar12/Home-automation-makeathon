query_stream = None
oldFlag = False

def query_handler(message):
    global oldFlag
    if not oldFlag:
        oldFlag = True
    else:
        print(str(message["data"]))
        if str(message["data"]):
            wit.test(str(message["data"]))

def set_stream(db, id):
    query_stream = db.child("Query").stream(query_handler, id, stream_id="changes")
