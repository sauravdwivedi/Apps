# Flutter application to fetch SEK to INR

<img src=pic.PNG alt="iOS simulator image" width="300">

## Project description

The application is written in Flutter. Application makes API call to endpoint:

- https://api.apilayer.com/currency_data/convert

and returns exchange value for SEK to INR.

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

Install flutter:

- https://docs.flutter.dev/get-started/install/macos
  
```bash
$ gh repo clone sauravdwivedi/Apps
$ cd Apps && cd Flutter && cd currency_conversion
$ open -a Simulator
$ flutter run
```
