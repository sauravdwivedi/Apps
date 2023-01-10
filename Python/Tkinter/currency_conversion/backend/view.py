import tkinter as tk
from backend import logger


class View(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.frame_label = tk.Frame(relief=tk.SUNKEN, borderwidth=0)
        self.frame_label.grid(row=0, column=0, padx=5, pady=5)

        self.frame_buttons = tk.Frame(relief=tk.RIDGE, borderwidth=0)
        self.frame_buttons.grid(row=0, column=1, padx=5, pady=5)

        self.rate_label = tk.Label(master=self.frame_label, text="1 SEK = {rate} INR")
        self.rate_label.pack()

        self.time_label = tk.Label(master=self.frame_label, text="at {time}")
        self.time_label.pack()

        self.next_ex_label = tk.Label(
            master=self.frame_label,
            text="Next execution: {next_execution}",
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

    def start_application(self):
        self.controller.start_application()

    def refresh_button_clicked(self):
        if self.controller:
            self.controller.refresh_button_clicked()

    def close_application(self):
        if self.controller:
            self.controller.close_application()
