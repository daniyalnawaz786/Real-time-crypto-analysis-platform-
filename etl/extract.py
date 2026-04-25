from api.fetch_data import fetch_crypto_data

def extract_data():
    coins = ["bitcoin", "ethereum", "solana"]
    data = fetch_crypto_data(coins)
    return data