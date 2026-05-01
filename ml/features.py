def add_features(df):
    df = df.copy()

    df["returns"] = df["price"].pct_change()

    df["ma_5"] = df["price"].rolling(5).mean()
    df["ma_10"] = df["price"].rolling(10).mean()

    df["volatility"] = df["returns"].rolling(5).std()

    df["ma_diff"] = df["ma_5"] - df["ma_10"]

    df["target"] = (df["price"].shift(-1) > df["price"]).astype(int)

    df = df.dropna()

    return df