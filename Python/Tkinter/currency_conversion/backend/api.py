import requests
import json
from backend import Config, logger
from requests.exceptions import HTTPError


class CurrencyConversionAPI:
    def get(self) -> dict:
        url: str = (
            "https://api.apilayer.com/currency_data/convert?to=INR&from=SEK&amount=1"
        )
        payload: dict = {}
        headers: dict = {"apikey": Config.SECRET}
        try:
            response: any = requests.request("GET", url, headers=headers, data=payload)
        except HTTPError as e:
            logger.error("Error ocurred while API call %s", e)
            raise HTTPError("API call failed")
        except AttributeError as e:
            raise AttributeError
        else:
            status_code: int = response.status_code
            info: dict = json.loads(response.content.decode("utf-8")).get("info")

        return {"info": info, "status_code": status_code}
