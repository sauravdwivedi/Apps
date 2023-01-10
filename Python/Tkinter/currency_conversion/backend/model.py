import datetime
from backend import CurrencyConversionAPI, CurrencyConversionScheduler, logger


class Model:
    def __init__(self) -> None:
        rate, time = self.api_call()
        self.rate = rate
        self.time = time
        self.schedule = CurrencyConversionScheduler(
            scheduler_enabled=True, scheduler_cron="0 11 * * *"
        )
        self.next_execution = self.schedule.next_execution

    def api_call(self) -> tuple:
        result: dict = CurrencyConversionAPI().get()

        if result.get("info"):
            rate: str = result.get("info").get("quote")
            time: str = datetime.datetime.fromtimestamp(
                result.get("info").get("timestamp")
            )
            logger.info(f"SEK to INR at {time}: {rate}")
        else:
            rate: str = "NULL"
            time: str = "NULL"
            logger.error(f"An error ocurred in API call!")

        return rate, time
