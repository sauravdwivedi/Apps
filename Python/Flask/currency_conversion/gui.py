#! /usr/bin/python3

import tkinter as tk
import datetime
import logging
from backend import CurrencyConversionAPI, CurrencyConversionScheduler


logging.getLogger(__name__)


class Model:
    def __init__(self) -> None:
        global rate, time, next_execution
        rate, time = self.api_call()
        self.rate = rate
        self.time = time
        self.schedule = CurrencyConversionScheduler(
            scheduler_enabled=True, scheduler_cron="0 11 * * *"
        )
        next_execution = self.schedule.next_execution

    def api_call(self) -> tuple:
        result: dict = CurrencyConversionAPI().get()

        if result.get("info"):
            rate: str = result.get("info").get("quote")
            time: str = datetime.datetime.fromtimestamp(
                result.get("info").get("timestamp")
            )
            logging.info(f"SEK to INR at {time}: {rate}")
        else:
            rate: str = "NULL"
            time: str = "NULL"
            logging.error(f"An error ocurred in API call!")

        return rate, time


class View(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.frame_label = tk.Frame(relief=tk.SUNKEN, borderwidth=0)
        self.frame_label.grid(row=0, column=0, padx=5, pady=5)

        self.frame_buttons = tk.Frame(relief=tk.RIDGE, borderwidth=0)
        self.frame_buttons.grid(row=0, column=1, padx=5, pady=5)

        self.rate_label = tk.Label(master=self.frame_label, text=f"1 SEK = {rate} INR")
        self.rate_label.pack()

        self.time_label = tk.Label(master=self.frame_label, text=f"at {time}")
        self.time_label.pack()

        self.next_ex_label = tk.Label(
            master=self.frame_label, text=f"Next execution: {next_execution}"
        )
        self.next_ex_label.pack()

        self.get_button = tk.Button(
            master=self.frame_buttons,
            width=5,
            text="Refresh",
            fg="green",
            command=self.refresh_button_clicked,
        )
        self.get_button.grid(row=0, column=0)

        self.close_button = tk.Button(
            master=self.frame_buttons,
            text="Close",
            width=5,
            fg="red",
            command=self.close_application,
        )
        self.close_button.grid(row=1, column=0)

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def refresh_button_clicked(self):
        if self.controller:
            self.controller.refresh_button_clicked()

    def close_application(self):
        if self.controller:
            self.controller.close_application()


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def refresh_button_clicked(self):
        self.view.next_ex_label[
            "text"
        ] = f"Next execution: {self.model.schedule.next_execution}"

        if self.model.schedule.result:
            self.view.rate_label[
                "text"
            ] = f"1 SEK = {self.model.schedule.result.get('quote')} INR"
            self.view.time_label[
                "text"
            ] = f"at {datetime.datetime.fromtimestamp(self.model.schedule.result.get('timestamp'))}"

    def close_application(self):
        self.model.schedule.disable()
        logging.info(f"Closing application")
        raise SystemExit


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SKE to INR conversion rate")
        self.geometry("350x150")

        model: Model = Model()
        view: View = View(self)
        view.grid(row=0, column=0)
        controller: Controller = Controller(model, view)

        view.set_controller(controller)


def main() -> None:
    app: App = App()
    app.mainloop()


if __name__ == "__main__":
    main()
