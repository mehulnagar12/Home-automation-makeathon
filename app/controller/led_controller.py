import modules.led as led

#Turn all LEDs ON
def turnAllOn():
    for i in range(1,4):
        led.setLED(i, 100)

#Turn all LEDs OFF
def turnAllOff():
    for i in range(1,4):
        led.setLED(i, 0)

#task is in the format (led_num, value)
def turnLED(task):
    led.setLED(task[0], task[1])
