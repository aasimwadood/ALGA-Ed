
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
import os

def anonymize_data(df):
    if 'user_id' in df.columns:
        df['user_id'] = df['user_id'].astype(str).apply(lambda x: hash(x))
    return df

def annotate_data(df, disability_type=None):
    if disability_type:
        df['disability_type'] = disability_type
        if disability_type == "visual":
            df['contrast_preference'] = 'high'
        elif disability_type == "auditory":
            df['audio_required'] = True
        elif disability_type == "cognitive":
            df['simplified_text'] = True
    return df

def preprocess_features(df, categorical_cols=None, numeric_cols=None):
    if categorical_cols:
        for col in categorical_cols:
            encoder = LabelEncoder()
            df[col] = encoder.fit_transform(df[col].astype(str))
    if numeric_cols:
        scaler = StandardScaler()
        df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    return df

def remove_incomplete_rows(df):
    return df.dropna()

def preprocess_dataset(path, disability_type=None, cat_cols=None, num_cols=None):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Dataset not found: {path}")
    df = pd.read_csv(path)
    df = anonymize_data(df)
    df = annotate_data(df, disability_type)
    df = preprocess_features(df, cat_cols, num_cols)
    df = remove_incomplete_rows(df)
    return df
