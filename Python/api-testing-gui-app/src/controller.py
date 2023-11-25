import tkinter as tk
import json


class Controller:
    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

    def start_view(self):
        self.view.make_frames()
        self.view.make_first_view()

    def api_call(self):
        self.view._result.delete("1.0", "end")
        endpoint = self.view._endpoint.get()

        if self.view.payload.get() == "Query Params":
            payload = ""

            if self.view._payload_key_one.get() != "":
                endpoint += (
                    "?"
                    + self.view._payload_key_one.get()
                    + "="
                    + self.view._payload_value_one.get()
                )
                self.view.endpoint_history.set(endpoint)

            if self.view._payload_key_two.get() != "":
                endpoint += (
                    "&"
                    + self.view._payload_key_two.get()
                    + "="
                    + self.view._payload_value_two.get()
                )
                self.view.endpoint_history.set(endpoint)

            if self.view._payload_key_three.get() != "":
                endpoint += (
                    "&"
                    + self.view._payload_key_three.get()
                    + "="
                    + self.view._payload_value_three.get()
                )
                self.view.endpoint_history.set(endpoint)

            if self.view._payload_key_four.get() != "":
                endpoint += (
                    "&"
                    + self.view._payload_key_four.get()
                    + "="
                    + self.view._payload_value_four.get()
                )
                self.view.endpoint_history.set(endpoint)

        with open("endpoints.txt", "r") as f:
            lines = [line.rstrip("\n") for line in f.readlines()]
            lines.append(endpoint)
            self.view._endpoint["values"] = sorted(tuple(set(lines)))

        with open("endpoints.txt", "w") as f:
            for line in self.view._endpoint["values"]:
                f.write(line + "\n")

        method = self.view._method

        if self.view.payload.get() == "JSON":
            payload = self.view._payload.get("1.0", "end-1c")

        if payload == "":
            payload = {}
        else:
            payload = json.loads(payload)

        token_uri = self.view._token_uri.get()
        client_id = self.view._client_id.get()
        username = self.view._username.get()
        password = self.view._password.get()

        try:
            self._response = self.model.api_call(
                endpoint, method, payload, token_uri, client_id, username, password
            )
        except Exception as e:
            if "code" in dir(e):
                self._response = {e.code: e.description}
            else:
                self._response = {500: repr(e)}

        if self._response in (None, {}):
            self._response = {204: "No content"}

        if type(self._response) != list:
            self._response = [self._response]

        self.display_response()

    def display_response(self):
        for item in self._response:
            self.view._result.insert(tk.END, "{\n    ")

            for k in item:
                self.view._result.insert(
                    tk.END,
                    "{}: {},\n    ".format(json.dumps(k), json.dumps(item[k])),
                )

            self.view._result.delete("end-7c", "end")
            self.view._result.insert(tk.END, "\n}\n")
