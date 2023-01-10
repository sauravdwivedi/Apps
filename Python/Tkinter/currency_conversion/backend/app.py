import tkinter as tk

from backend import Model, View, Controller


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
        view.start_application()


app: App = App()
