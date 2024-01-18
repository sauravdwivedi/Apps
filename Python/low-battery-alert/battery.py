from mac_alerts import alerts
import psutil
import time
import threading

WAITING_TIME = 3
MIN_CHARGE_PERCENT = 20


def check_battery():
    while True:
        if (
            not psutil.sensors_battery().power_plugged
            and psutil.sensors_battery().percent <= MIN_CHARGE_PERCENT
        ):
            trigger_alert()
            time.sleep(WAITING_TIME)


def trigger_alert():
    alerts.play_error()
    print("Need to connect battery")


if __name__ == "__main__":
    hb = threading.Thread(target=check_battery, daemon=False)
    hb.start()
