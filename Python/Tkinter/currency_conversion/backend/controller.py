import datetime
from backend import Model, View, logger


class Controller:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

    def start_application(self):
        self.view.rate_label["text"] = f"1 SEK = {self.model.rate} INR"
        self.view.time_label["text"] = f"at {self.model.time}"
        self.view.next_ex_label["text"] = f"Next execution: {self.model.next_execution}"

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
        logger.info(f"Closing application")
        self.view.destroy
        raise SystemExit
