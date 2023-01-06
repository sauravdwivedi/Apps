# Flask application to schedule currency conversion

## Project description

Flask application makes API call to endpoint:

- https://api.apilayer.com/currency_data/convert

and returns exchange value for SEK to INR. The application uses CRON scheduler to enable fetching exchange rate data at a desired schedule, currently set for 11 AM local time everyday.

## API Call

### GET request
```bash
curl --request GET \
--url 'https://api.apilayer.com/currency_data/convert?to=INR&from=SEK&amount=1' \
--header 'apikey: mPeEQPVuAtxVR2LFYXAlRclZtbGApyOh'
```

### Response
```json
{
    "success": true,
    "query": {
        "from": "SEK",
        "to": "INR",
        "amount": 1
    },
    "info": {
        "timestamp": 1673033643,
        "rate": 7.815987
    },
    "date": "2023-01-06",
    "result": 7.815987
}
```


## Execution

### Run code
  
```bash
$ gh repo clone sauravdwivedi/Apps
$ cd Apps && cd Python && cd Flask && cd currency_conversion
$ python3 -m venv currency_conv
$ source currency_conv/bin/activate
$ pip3 install -r requirements.txt
$ source secrets
$ export FLASK_APP=app
$ flask run
```

### Open app in browser (and refresh for up-to-date value)

- http://127.0.0.1:5000/

