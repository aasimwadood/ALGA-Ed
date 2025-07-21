import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(path):
    df = pd.read_csv(path)
    X = df.drop("engagement", axis=1).values
    y = df["engagement"].values
    return X, y

def preprocess(X):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled