import requests
from werkzeug.exceptions import Unauthorized, BadRequest
from datetime import datetime


class Model:
    def api_call(
        self,
        endpoint,
        method,
        payload,
        token_uri,
        client_id,
        username,
        password,
        token="",
    ):
        try:
            if not (endpoint and method):
                raise BadRequest("Endpoint and/or method missing")

            if token_uri and client_id and username and password:
                token = self.get_token(token_uri, client_id, username, password)

            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + token,
            }

            if method == "GET":
                response = requests.get(url=endpoint, json=payload, headers=headers)

            if method == "POST":
                response = requests.post(url=endpoint, json=payload, headers=headers)

            if method == "PUT":
                response = requests.put(url=endpoint, json=payload, headers=headers)

            if method == "PATCH":
                response = requests.patch(url=endpoint, json=payload, headers=headers)

            if method == "DELETE":
                response = requests.delete(url=endpoint, json=payload, headers=headers)

            return response.json()

        except Exception:
            raise

    def get_token(self, token_uri, client_id, username, password):
        try:
            token_response = requests.post(
                token_uri,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                data={
                    "grant_type": "password",
                    "client_id": client_id,
                    "username": username,
                    "password": password,
                },
            )

            if token_response.status_code == 200:
                print(f"{datetime.now()}: Access token obtained")
                return token_response.json()["access_token"]
            else:
                raise Unauthorized("Error ocurred in obtaining access token")
        except Exception:
            raise
