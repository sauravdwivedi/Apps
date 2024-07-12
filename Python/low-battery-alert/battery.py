#!/usr/bin/python3
from mac_alerts import alerts
import psutil
import time
import threading
import os

WAITING_TIME = 3
MIN_CHARGE_PERCENT = 20
MAX_CHARGE_PERCENT = 80


def check_battery():
    
    while True:
        if psutil.sensors_battery().power_plugged:
            if psutil.sensors_battery().percent >= MAX_CHARGE_PERCENT:
                print("Disconnect charger")
                trigger_alert()
                push_notification("disconnect")
                time.sleep(WAITING_TIME)
        else:
            if psutil.sensors_battery().percent <= MIN_CHARGE_PERCENT:
                print("Connect charger")
                trigger_alert()
                push_notification("connect")
                time.sleep(WAITING_TIME)


def trigger_alert():
    alerts.play_error()
    
def push_notification(message):
    if message == "connect":
        os.system("""osascript -e 'display notification "Battery is low, please connect charger" with title "Battery alert!"'""")
    if message == "disconnect":
        os.system("""osascript -e 'display notification "Battery is full, please disconnect charger" with title "Battery alert!"'""")


if __name__ == "__main__":
    hb = threading.Thread(target=check_battery, daemon=False)
    hb.start()
