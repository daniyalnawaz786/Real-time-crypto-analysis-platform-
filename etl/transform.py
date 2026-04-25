from datetime import datetime

def transform_data(raw_data):
    transformed = []

    for coin, values in raw_data.items():
        transformed.append({
            "coin_name": coin,
            "price": values.get("usd", 0),
            "change_24h": values.get("usd_24h_change", 0),
            "timestamp": str(datetime.now())
        })

    return transformed