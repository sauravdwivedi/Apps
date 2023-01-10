# Python GUI application to schedule currency conversion

## Project description

GUI application using Python GUI framework Tkinter makes API call to endpoint:

- https://api.apilayer.com/currency_data/convert

and returns exchange value for SEK to INR. The application uses CRON scheduler to enable fetching exchange rate data at a desired schedule, currently set for 11 AM local time everyday.

## API Call

### GET request
```bash
curl --request GET \
--url 'https://api.apilayer.com/currency_data/convert?to=INR&from=SEK&amount=1' \
--header 'apikey: lWHgvT1oGQVVxprbrVswsTroUUG2DYYj'
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
        "timestamp": 1673116982,
        "quote": 7.818749
    },
    "result": 7.818749
}
```


## Execution

### Run code
  
```bash
$ gh repo clone sauravdwivedi/Apps
$ cd Apps && cd Python && cd Tkinter && cd currency_conversion
$ brew install python-tk
$ python3 -m venv currency_conv
$ source currency_conv/bin/activate
$ pip3 install -r requirements.txt
$ source secrets
$ python3 app.py
```