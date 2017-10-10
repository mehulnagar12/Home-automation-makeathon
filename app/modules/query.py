import config
import controller.wit_controller as wit

def init():
    global oldFlag
    oldFlag = False

def query_handler(message):
    global oldFlag
    if not oldFlag:
        oldFlag = True
    else:
        print(str(message["data"]))
        if str(message["data"]):
            wit.test(str(message["data"]))

def setStream():
    query_stream = config.db.child("Query").stream(query_handler, config.id, stream_id="changes")
