
from sklearn.metrics import accuracy_score, classification_report
import joblib

def evaluate_model(X_test, y_test, model_path):
    model = joblib.load(model_path)
    y_pred = model.predict(X_test)
    print("Evaluation Report:")
    print(classification_report(y_test, y_pred))
    return accuracy_score(y_test, y_pred)

if __name__ == "__main__":
    import argparse
    import pandas as pd
    from sklearn.model_selection import train_test_split
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    args = parser.parse_args()

    data = pd.read_csv(args.input)
    X = data.drop("label", axis=1)
    y = data["label"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    evaluate_model(X_test, y_test, "outputs/model.joblib")
