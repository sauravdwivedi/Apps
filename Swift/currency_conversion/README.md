# Swift iOS application to fetch currency conversion rate

<img src=pic.PNG alt="iOS simulator image" width="300">

## Project description

The application is written in Swift. Application makes API call to endpoint:

- https://api.apilayer.com/exchangerates_data/convert

and returns exchange value for SEK to INR

## API Call

### GET request 
```bash
curl --request GET 'https://api.apilayer.com/exchangerates_data/symbols' \                  
--header 'apikey: mPeEQPVuAtxVR2LFYXAlRclZtbGApyOh'
```

### Response

```json
{
    "success": true,
    "symbols": {
        "AED": "United Arab Emirates Dirham",
        "AFN": "Afghan Afghani",
        "ALL": "Albanian Lek",
        "AMD": "Armenian Dram",
        "ANG": "Netherlands Antillean Guilder",
        .
        .
        .
    }
}
```

### GET request
```bash
curl --request GET \
--url 'https://api.apilayer.com/exchangerates_data/convert?to=INR&from=SEK&amount=1' \
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
        "timestamp": 1674308103,
        "rate": 7.865205
    },
    "date": "2023-01-21",
    "result": 7.865205
}
```

## Execution

```bash
$ gh repo clone sauravdwivedi/Apps
$ cd Apps && cd Swift && cd currency_conversion
```

Open project in Xcode, and build ( <kbd>⌥</kbd> + <kbd>⌘</kbd> + <kbd>P</kbd> ).