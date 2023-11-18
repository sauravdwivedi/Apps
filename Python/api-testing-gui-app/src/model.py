import requests


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
                if not self.token:
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
                headers={"Content-Type": "application/json"},
                data={
                    "grant_type": "client_credentials",
                    "client_id": client_id,
                    "client_secret": password,
                },
            )

            print(token_response.json())

            if token_response.status_code == 200:
                print("Access token obtained")
                return token_response.json()["access_token"]
        except Exception:
            raise
