import requests
from werkzeug.exceptions import Unauthorized, NotFound, BadRequest, InternalServerError


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
                response = requests.get(url=endpoint, data=payload, headers=headers)

            if method == "POST":
                response = requests.post(url=endpoint, data=payload, headers=headers)

            if response.status_code == 404:
                raise NotFound

            if response.status_code == 401:
                raise Unauthorized

            if response.status_code == 500:
                raise InternalServerError

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
                print("Access token obtained")
                return token_response.json()["access_token"]
            else:
                raise Unauthorized("Error ocurred in obtaining access token")
        except Exception:
            raise
