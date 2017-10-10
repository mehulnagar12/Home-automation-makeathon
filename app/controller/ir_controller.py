import modules.infrared as infrared

#Turn AC ON
def turnOn():
    infrared.setValue(1)

#Turn AC OFF
def turnOff():
    infrared.setValue(0)
