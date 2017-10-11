import config
import controller.serial_controller as serial_controller

def init():
    global oldFlag
    oldFlag = False

def infra_handler(message):
    global oldFlag
    if not oldFlag:
        oldFlag = True
    else:
        #To ensure single hits from WIT
        if config.wittyIR==True:
            config.wittyIR = False
        else:
            print("AC "+str(message["data"]))
            serial_controller.setIR(message["data"])

def setStream():
    infra_stream = config.db.child("Sensor").child("AC").stream(infra_handler, config.id, stream_id="ac")

def setValue(data):
    serial_controller.setIR(data)
    config.db.child("Sensor").child("AC").push(data, config.id)
