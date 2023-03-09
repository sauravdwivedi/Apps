# Vue application to fetch conversion rate

<img src=pic.PNG alt="Vue application image">

## Project description

The application is written in Vue 3. Application makes API call to endpoint:

- https://api.apilayer.com/currency_data/convert

and returns exchange value for two chosen currencies from dropdown list. Application first makes API call to fetch available currencies to populate dropdown lists.

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

```bash
gh repo clone sauravdwivedi/Apps
cd Apps && cd Vue && cd currency_conversion
brew install node
npm install axios
npm install moment
npm run serve
```

### Open in browser (and click refresh for up-to-date value)

- http://localhost:8080/
