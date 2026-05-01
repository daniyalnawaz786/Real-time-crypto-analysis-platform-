import time
from api.fetch_data import fetch_crypto_data
from utils.converter import convert_to_dataframe, save_to_csv

COINS = ["bitcoin", "ethereum"]

def run():
    while True:
        print("Fetching crypto data...")

        data = fetch_crypto_data(COINS)

        if data:
            df = convert_to_dataframe(data)
            save_to_csv(df)
            print("Saved:\n", df)

        time.sleep(60)  # every 60 sec


if __name__ == "__main__":
    run()