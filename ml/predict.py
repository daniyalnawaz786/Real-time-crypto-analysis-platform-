import joblib
from ml.features import add_features

model = joblib.load("ml/model.pkl")

def predict_signal(df):
    df = add_features(df)

    latest = df.iloc[-1:]

    X = latest[["returns", "ma_5", "ma_10", "volatility", "ma_diff"]]

    pred = model.predict(X)[0]

    return "BUY 📈" if pred == 1 else "SELL 📉"