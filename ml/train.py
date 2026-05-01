from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

from ml.data_loader import load_data
from ml.features import add_features

def train():
    df = load_data()
    df = add_features(df)

    X = df[["returns", "ma_5", "ma_10", "volatility", "ma_diff"]]
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    acc = model.score(X_test, y_test)
    print("Accuracy:", acc)

    joblib.dump(model, "ml/model.pkl")


if __name__ == "__main__":
    train()