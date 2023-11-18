from src.model import Model


class Controller:
    def __init__(self) -> None:
        self.model = Model()

    def api_call(
        self, endpoint, method, payload, token_uri, client_id, username, password
    ):
        try:
            result = self.model.api_call(
                endpoint, method, payload, token_uri, client_id, username, password
            )
        except Exception:
            raise

        return result
