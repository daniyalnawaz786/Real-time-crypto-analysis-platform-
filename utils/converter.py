import pandas as pd
from datetime import datetime
import os

def convert_to_dataframe(data):
    rows = []

    for coin, values in data.items():
        rows.append({
            "coin": coin,
            "price": values["usd"],
            "change_24h": values.get("usd_24h_change", 0),
            "timestamp": datetime.utcnow()
        })

    return pd.DataFrame(rows)


def save_to_csv(df, filename="data/crypto_prices.csv"):
    os.makedirs("data", exist_ok=True)

    file_exists = os.path.isfile(filename)

    df.to_csv(
        filename,
        mode="a",
        header=not file_exists,
        index=False
    )