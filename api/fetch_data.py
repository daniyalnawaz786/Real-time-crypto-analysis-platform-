import requests

BASE_URL = "https://api.coingecko.com/api/v3/simple/price"

def fetch_crypto_data(coins):
    params = {
        "ids": ",".join(coins),
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }

    response = requests.get(BASE_URL, params=params)
    
    if response.status_code != 200:
        print("API Error:", response.text)
        return None

    return response.json()