#! /usr/bin/python3

from flask import Flask, render_template
import datetime
import logging
from backend import Config, CurrencyConversionScheduler, CurrencyConversionAPI


app: Flask = Flask(__name__, template_folder="templates")
app.config.from_object(Config)

logging.getLogger(__name__)


@app.route("/")
def home() -> any:
    next_execution = app.currency_conversion_scheduler.next_execution
    title = "SEK to INR conversion rate"

    if app.currency_conversion_scheduler.result:
        timestamp: any = app.currency_conversion_scheduler.result.get("timestamp")
        timestamp: str = datetime.datetime.fromtimestamp(timestamp)
        rate = app.currency_conversion_scheduler.result.get("quote")
    else:
        response = CurrencyConversionAPI().get()
        if response.get("info"):
            response = response.get("info")
            timestamp_raw = response.get("timestamp")
            timestamp: str = datetime.datetime.fromtimestamp(timestamp_raw)
            rate = response.get("quote")
            app.currency_conversion_scheduler.result = {
                "timestamp": timestamp_raw,
                "quote": rate,
            }
        else:
            timestamp = "NULL"
            rate = "NULL"
            title = "An error ocurred in API call!"

    return render_template(
        "index.html",
        title=title,
        execution_time=timestamp,
        next_execution=next_execution,
        exchange_rate=rate,
    )


@app.before_first_request
def add_schedulers() -> None:
    if not hasattr(app, "currency_conversion_scheduler"):
        app.currency_conversion_scheduler = CurrencyConversionScheduler(
            scheduler_enabled=True, scheduler_cron="0 11 * * *"
        )


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="localhost")
