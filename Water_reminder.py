import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "hey please drink water",
            message = "Getting enough water every day is important for your health. Drinking water can prevent dehydration, a condition that can cause unclear thinking, result in mood change, cause your body to overheat, and lead to constipation and kidney stones. Water helps your body: Keep a normal temperature",
            app_icon = "E:\Projects\water.ico",
            timeout = 12
        )
        