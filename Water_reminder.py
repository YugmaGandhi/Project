from email import message
import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "hey please drink water",
            message = "water is very important for body and it keeps you hydrated", #remerber to type message that is not longer than 256 char
            app_icon = "E:\Projects\water.ico",
            timeout = 12
        )
    
        time.sleep(60*60)