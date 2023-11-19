import requests
from werkzeug.exceptions import Unauthorized


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
            if token_uri and client_id and username and password:
                token = self.get_token(token_uri, client_id, username, password)
                if not token:
                    return {"Response": "Token not found"}

            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + token,
            }

            if method == "GET":
                return requests.get(url=endpoint, data=payload, headers=headers).json()

            if method == "POST":
                return requests.post(url=endpoint, data=payload, headers=headers).json()

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
                raise Unauthorized("Access token not obtained")
        except Exception:
            raise
