#Read and write serial data with Arduino
import serial, _thread
import modules.hall as hall
import modules.temperature as temp
import modules.smoke as smoke

def init():
    global s1, s2
    s1 = serial.Serial('/dev/ttyACM0', 250000) #LED and IR
    s2 = serial.Serial('/dev/ttyACM1', 250000) #Temp, Hall and Smoke

def setRead():
    s2.readline()
    while 1:
        data = s2.readline().decode('utf-8')
        data = str(data).split('\r\n')[0]
        data = data.split(',')
        #temp hall smoke
        temp.setValue(data[0])
        hall.setValue(data[1])
        smoke.setValue(data[2])

def setListenOn():
    _thread.start_new_thread(setRead, ())

def setLED(number, value):
    #Write LED
    toWrite = '0'+str(number)+':'+str(value)
    s1.write(toWrite.encode('utf-8'))

def setIR(value):
    #Write IR blaster
    value+=1 #Normalize
    toWrite = '06:'+ str(value)
    s1.write(toWrite.encode('utf-8'))
