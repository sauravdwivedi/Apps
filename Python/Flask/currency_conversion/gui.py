#! /usr/bin/python3

import tkinter as tk
import datetime
import logging
from backend import CurrencyConversionAPI


logging.getLogger(__name__)


class Model:
    def __init__(self) -> None:
        global rate, time
        rate, time = self.api_call()
        self.rate = rate
        self.time = time

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
        rate, time = self.model.api_call()
        self.view.rate_label["text"] = f"1 SEK = {rate} INR"
        self.view.time_label["text"] = f"at {time}"

    def close_application(self):
        exit()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SKE to INR conversion rate")
        self.geometry("300x150")

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
