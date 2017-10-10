import os, pyrebase
import controller.wit_controller as wit
import modules.hall as hall
import modules.led as led
import modules.infrared as infra
import modules.temperature as temp

oldFlag = False
config =  {
    "apiKey": os.environ["API_FIREBASE"],
    "authDomain": "piedpiper-home.firebaseapp.com",
    "databaseURL": "https://piedpiper-home.firebaseio.com",
    "projectId": "piedpiper-home",
    "storageBucket": "piedpiper-home.appspot.com"
}

## check
if(config["apiKey"]==None):
    print("Error in APIkey")
    os._exit(0)

firebase = pyrebase.initialize_app(config)
#Initialize auth/database
auth = firebase.auth()
db = firebase.database()

#login
user = None
try:
    print("Logging in...")
    user = auth.sign_in_with_email_and_password(os.environ["EMAIL_FIREBASE"], os.environ["PASSWORD_FIREBASE"])
    print("Logged in...")
except Exception as e:
    if "EMAIL_NOT_FOUND" in str(e):
        print("Check environment EMAIL_FIREBASE")
    else:
        print(e)
    os._exit(0)

print("Listening to Modules...")
hall.setStream(db, user["idToken"])
led.setStream(db, user["idToken"])
infra.setStream(db, user["idToken"])
temp.setStream(db, user["idToken"])
query.setStream(db, user["idToken"])
