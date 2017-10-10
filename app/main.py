import os, pyrebase
import config as configFile
import modules.hall as hall
import modules.led as led
import modules.infrared as infra
import modules.temperature as temp
import modules.query as query
import modules.smoke as smoke

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

configFile.init(db, user["idToken"])
print("Listening to Modules...")
hall.init(); hall.setStream()
led.init(); led.setStream()
infra.init(); infra.setStream()
temp.init(); temp.setStream()
query.init(); query.setStream()
smoke.init(); smoke.setStream()
