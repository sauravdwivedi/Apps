# Angular application to plot currency conversion historical data

<img src=pic.PNG alt="Angular application image">

## Project description

The application is written in Type Script web framework Angular. Application makes API call to ApiLayer:

- https://apilayer.com/marketplace/exchangerates_data-api

and returns exchange value for two chosen currencies from dropdown list for chosen dates range. Application first makes API call to fetch available currencies to populate dropdown lists.

## API Call

### GET request 
```bash
curl --request GET 'https://api.apilayer.com/currency_data/list' \                  
--header 'apikey: lWHgvT1oGQVVxprbrVswsTroUUG2DYYj'
```

### Response

```json
{
    "success": true,
    "currencies": {
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
curl --request GET 'https://api.apilayer.com/exchangerates_data/timeseries?start_date=2023-02-20&end_date=2023-02-23&base=SEK&symbols=INR' \
--header 'apikey: lWHgvT1oGQVVxprbrVswsTroUUG2DYYj'
```

### Response
```json
{
    "success": true,
    "timeseries": true,
    "start_date": "2023-02-20",
    "end_date": "2023-02-23",
    "base": "SEK",
    "rates": {
        "2023-02-20": {
            "INR": 7.992784
        },
        "2023-02-21": {
            "INR": 7.986168
        },
        "2023-02-22": {
            "INR": 7.9483
        },
        "2023-02-23": {
            "INR": 7.920749
        }
    }
}
```

## Execution

```bash
gh repo clone sauravdwivedi/Apps
cd Apps && cd Angular && cd currency_conversion
brew install node
npm install axios
npm install -g @angular/cli
npm install @angular-devkit/build-angular
ng add @angular/material
ng serve
```

### Open in browser (and click refresh for making another conversion)

- http://localhost:4200/
