import tkinter as tk
from tkinter import ttk
import os


class View:
    def __init__(self, name):
        self.root = tk.Tk()
        self.root.title = name
        # self.root.geometry("900x600")
        self.name = name
        self._method = ""

    def set_controller(self, controller):
        self.controller = controller

    def start_view(self):
        self.controller.start_view()

    def make_frames(self):
        self.api_frame = tk.Frame(self.root, width=900, height=300, relief=tk.SUNKEN)
        self.response_frame = tk.Frame(
            self.root, width=900, height=300, relief=tk.SUNKEN
        )

        # Pack frames to root window in following order
        self.api_frame.pack()
        self.response_frame.pack()

    def make_first_view(self):
        tk.Label(self.api_frame, text="endpoint").place(x=10, y=10)
        tk.Label(self.api_frame, text="method").place(x=10, y=40)
        tk.Label(self.api_frame, text="payload").place(x=10, y=70)
        tk.Label(self.api_frame, text="token uri").place(x=550, y=10)
        tk.Label(self.api_frame, text="client-id").place(x=550, y=40)
        tk.Label(self.api_frame, text="username").place(x=550, y=70)
        tk.Label(self.api_frame, text="password").place(x=550, y=100)
        self.endpoint_history = tk.StringVar()
        self._endpoint = ttk.Combobox(
            self.api_frame, width=45, textvariable=self.endpoint_history
        )
        self.method = tk.StringVar()
        self._method_one = tk.Checkbutton(
            self.api_frame,
            text="GET",
            variable=self.method,
            onvalue="GET",
            offvalue="",
            command=self.method_changed,
        )
        self._method_two = tk.Checkbutton(
            self.api_frame,
            text="POST",
            variable=self.method,
            onvalue="POST",
            offvalue="",
            command=self.method_changed,
        )
        self._method_three = tk.Checkbutton(
            self.api_frame,
            text="PUT",
            variable=self.method,
            onvalue="PUT",
            offvalue="",
            command=self.method_changed,
        )
        self._method_four = tk.Checkbutton(
            self.api_frame,
            text="PATCH",
            variable=self.method,
            onvalue="PATCH",
            offvalue="",
            command=self.method_changed,
        )
        self._method_five = tk.Checkbutton(
            self.api_frame,
            text="DELETE",
            variable=self.method,
            onvalue="DELETE",
            offvalue="",
            command=self.method_changed,
        )
        self._payload = tk.Text(self.api_frame, height=15, width=55, padx=2, pady=2)
        self._token_uri = tk.Entry(self.api_frame)
        self._client_id = tk.Entry(self.api_frame)
        self._username = tk.Entry(self.api_frame)
        self._password = tk.Entry(self.api_frame, show="*")
        self.submit = tk.Button(
            self.api_frame,
            text="send",
            fg="Purple",
            bg="Red",
            command=self.api_call,
        )
        self._result = tk.Text(self.response_frame, width=100)
        self._endpoint.place(x=90, y=10)
        self._method_one.place(x=90, y=40)
        self._method_two.place(x=150, y=40)
        self._method_three.place(x=220, y=40)
        self._method_four.place(x=280, y=40)
        self._method_five.place(x=360, y=40)
        self._payload.place(x=90, y=70)
        self._token_uri.place(x=630, y=10)
        self._client_id.place(x=630, y=40)
        self._username.place(x=630, y=70)
        self._password.place(x=630, y=100)
        self.submit.place(x=630, y=180)
        self._result.place(x=50, y=0)

        # Populate default values from environment
        with open("./endpoints.txt", "a") as f:
            f.write(
                os.getenv("ENDPOINT", "https://jsonplaceholder.typicode.com/todos")
                + "\n"
            )

        with open("./endpoints.txt") as f:
            lines = [line.rstrip("\n") for line in f.readlines()]
            self._endpoint["values"] = sorted(tuple(set(lines)))

        self._token_uri.insert(
            0,
            os.getenv(
                "TOKEN_URI",
                "http://localhost:8080/realms/test/protocol/openid-connect/token",
            ),
        )

        self._endpoint.current(0)
        self._client_id.insert(0, os.getenv("CLIENT_ID", "api-testing-gui-app"))
        self._username.insert(0, os.getenv("USERNAME", "sdwivedi"))

    def method_changed(self):
        self._method = self.method.get()

    def api_call(self):
        self.controller.api_call()
