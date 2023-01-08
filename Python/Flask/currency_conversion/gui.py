#! /usr/bin/python3

import tkinter as tk
import datetime
from functools import partial
import logging
from backend import CurrencyConversionAPI


logging.getLogger(__name__)


def api_call() -> tuple:
    result: dict = CurrencyConversionAPI().get()

    if result.get("info"):
        rate: str = result.get("info").get("quote")
        time: str = datetime.datetime.fromtimestamp(result.get("info").get("timestamp"))
        logging.info(f"SEK to INR at {time}: {rate}")
    else:
        rate: str = "NULL"
        time: str = "NULL"
        logging.error(f"An error ocurred in API call!")

    return rate, time


def refresh_api_call(rate_label: str, rate_time: str) -> None:
    rate, time = api_call()
    rate_label["text"] = f"1 SEK = {rate} INR"
    rate_time["text"] = f"at {time}"


def sek_to_inr(main_window: tk.Tk, rate: str, time: str) -> None:
    main_window.title("SKE to INR conversion rate")
    main_window.geometry("300x150")

    frame_label = tk.Frame(master=main_window, relief=tk.SUNKEN, borderwidth=0)
    frame_label.grid(row=0, column=0, padx=5, pady=5)

    frame_buttons = tk.Frame(master=main_window, relief=tk.RIDGE, borderwidth=0)
    frame_buttons.grid(row=0, column=1, padx=5, pady=5)

    rate_label = tk.Label(master=frame_label, text=f"1 SEK = {rate} INR")
    rate_label.pack()

    time_label = tk.Label(master=frame_label, text=f"at {time}")
    time_label.pack()

    refresh_api_call_with_args = partial(refresh_api_call, rate_label, time_label)

    get_button = tk.Button(
        master=frame_buttons,
        width=5,
        text="Refresh",
        fg="green",
        command=refresh_api_call_with_args,
    )
    get_button.grid(row=0, column=0)

    close_button = tk.Button(
        master=frame_buttons,
        text="Close",
        width=5,
        fg="red",
        command=main_window.destroy,
    )
    close_button.grid(row=1, column=0)

    main_window.mainloop()


def main() -> None:
    main_window: tk.Tk = tk.Tk()
    result: tuple = api_call()
    sek_to_inr(main_window, *result)


if __name__ == "__main__":
    main()
