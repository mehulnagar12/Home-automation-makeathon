BUZZER_PIN = 12
Pi = False
import time, thread

try:
    import RPi.GPIO as GPIO
    Pi = True
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)
except:
    print("GPIO not found")

def alert(GPIO):
    GPIO.output(GPIO.HIGH)
    time.sleep(5)
    GPIO.output(GPIO.LOW)

def setAlarm(db):
    if not Pi:
        #Code is in dev
        print("Alarm set mock")
    else:
        #Code is in prod
        thread.start_new_thread(alert, (GPIO))
        db.child("Notif").setValue(0) #remove alert from db
