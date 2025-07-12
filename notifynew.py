import pandas as pd
import os

def load_previous_results(path="carlist.csv") -> pd.DataFrame:
    if os.path.exists(path):
        return pd.read_csv(path)
    return pd.DataFrame()

def save_results(df: pd.DataFrame, path="carlist.csv"):
    df.to_csv(path, index=False)
