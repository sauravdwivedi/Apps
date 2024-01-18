from mac_alerts import alerts
import psutil
import time
import threading

WAITING_TIME = 3
MIN_CHARGE_PERCENT = 20
MAX_CHARGE_PERCENT = 80


def check_battery():
    while True:
        if psutil.sensors_battery().power_plugged:
            if psutil.sensors_battery().percent >= MAX_CHARGE_PERCENT:
                print("Disconnect charger")
                trigger_alert()
                time.sleep(WAITING_TIME)
        else:
            if psutil.sensors_battery().percent <= MIN_CHARGE_PERCENT:
                print("Connect charger")
                trigger_alert()
                time.sleep(WAITING_TIME)


def trigger_alert():
    alerts.play_error()


if __name__ == "__main__":
    hb = threading.Thread(target=check_battery, daemon=False)
    hb.start()
