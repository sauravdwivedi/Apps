from src.controller import Controller
import tkinter as tk
import json
import os


class View:
    def __init__(self, name):
        self.controller = Controller()
        self.root = tk.Tk()
        self.root.title = name
        # self.root.geometry("900x600")
        self.name = name
        self.make_frames()
        self.make_first_view()
        self._method = ""

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
        tk.Label(self.api_frame, text="token uri").place(x=520, y=10)
        tk.Label(self.api_frame, text="client-id").place(x=520, y=40)
        tk.Label(self.api_frame, text="username").place(x=520, y=70)
        tk.Label(self.api_frame, text="password").place(x=520, y=100)
        self._endpoint = tk.Entry(self.api_frame, width=45)
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
        self._payload = tk.Text(self.api_frame, height=15, width=40, padx=2, pady=2)
        self._token_uri = tk.Entry(self.api_frame)
        self._client_id = tk.Entry(self.api_frame)
        self._username = tk.Entry(self.api_frame)
        self._password = tk.Entry(self.api_frame, show="*")
        self.submit = tk.Button(
            self.api_frame,
            text="submit",
            fg="Black",
            bg="Red",
            command=self.api_call,
        )
        self._endpoint.place(x=90, y=10)
        self._method_one.place(x=90, y=40)
        self._method_two.place(x=150, y=40)
        self._method_three.place(x=220, y=40)
        self._method_four.place(x=280, y=40)
        self._method_five.place(x=360, y=40)
        self._payload.place(x=90, y=70)
        self._token_uri.place(x=600, y=10)
        self._client_id.place(x=600, y=40)
        self._username.place(x=600, y=70)
        self._password.place(x=600, y=100)
        self.submit.place(x=600, y=180)

        # Populate default values from environment
        self._endpoint.insert(0, os.getenv("ENDPOINT"))
        self._token_uri.insert(0, os.getenv("TOKEN_URI"))
        self._client_id.insert(0, os.getenv("CLIENT_ID"))
        self._username.insert(0, os.getenv("USERNAME"))

    def method_changed(self):
        if self.method.get() == "GET":
            self._method = "GET"
        if self.method.get() == "POST":
            self._method = "POST"
        if self.method.get() == "PUT":
            self._method = "PUT"
        if self.method.get() == "PATCH":
            self._method = "PATCH"
        if self.method.get() == "DELETE":
            self._method = "DELETE"

    def api_call(self):
        endpoint = self._endpoint.get()
        method = self._method
        payload = json.dumps(self._payload.get("1.0", "end-1c"))
        token_uri = self._token_uri.get()
        client_id = self._client_id.get()
        username = self._username.get()
        password = self._password.get()
        print(f"Endpoint: {endpoint}\nMethod: {method}\nPayload: {payload}")
        try:
            response = self.controller.api_call(
                endpoint, method, payload, token_uri, client_id, username, password
            )
        except Exception:
            raise

        result = tk.Text(self.response_frame, width=100)
        result.place(x=50, y=0)

        if response == None:
            result.insert(tk.END, "{'Response': 'No response'}")
            result.config(state=tk.DISABLED)
            return

        if type(response) != list:
            response = [response]

        for item in response:
            result.insert(tk.END, "{\n    ")
            for k in item:
                result.insert(
                    tk.END, "{}: {}\n    ".format(json.dumps(k), json.dumps(item[k]))
                )
            result.delete("end-5c", "end")
            result.insert(tk.END, "\n}\n")

        result.config(state=tk.DISABLED)
