import datetime
import croniter
import threading
import logging

from backend import CurrencyConversionAPI

logging.getLogger(__name__)


class CronScheduler:
    def __init__(
        self,
        scheduler_enabled: bool = True,
        scheduler_cron: str = "0 12 * * *",
    ) -> None:
        self.scheduler_enabled = scheduler_enabled
        self.scheduler_cron = scheduler_cron
        self.next_execution = None
        self.result = None
        self.start()

    def start(self) -> None:
        now: any = datetime.datetime.now()
        itr: any = croniter.croniter(self.scheduler_cron, now)
        next_execution: any = itr.get_next(datetime.datetime)
        self.next_execution = next_execution
        lag: any = (next_execution - now).total_seconds()
        logging.info(f"Starting {self.__class__.__name__}")
        logging.info(f"Next execution: {next_execution}")
        # Setting new thread with timer and calling method action()
        self.thread_timer = threading.Timer(lag, self.start_action)
        # Starting thread with timer
        logging.info(f"Starting timer thread for {self.__class__.__name__}")
        self.thread_timer.start()
        # End of thread, calling start() again for next_execution

    def start_action(self) -> None:
        self.action()
        self.start()

    def action(self) -> None:
        pass

    def disable(self) -> None:
        self.stop()

    def stop(self) -> None:
        try:
            self.thread_timer.cancel()
            del self.thread_timer
        except AttributeError as e:
            logging.warning("Timer did not exist %s", e)


class CurrencyConversionScheduler(CronScheduler):
    def action(self) -> None:
        result: dict = CurrencyConversionAPI().get()
        if result.get("info"):
            result = result.get("info")
            now: any = datetime.datetime.now().strftime("%H:%M:%S %p")
            logging.info(f"SEK to INR at {now}: {result.get('quote')}")
            self.result = result
        else:
            logging.error("Error ocurred in API call!")
            return
