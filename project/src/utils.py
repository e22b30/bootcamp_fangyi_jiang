import pandas as pd
import os

def save_dataframe(df: pd.DataFrame, path: str, index: bool = False):
    """
    Save a DataFrame to CSV (creates directories if needed).
    
    Args:
        df (pd.DataFrame): DataFrame to save
        path (str): Path to save file (e.g., "data/processed/cleaned.csv")
        index (bool): Whether to include DataFrame index
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=index)
    print(f"✅ DataFrame saved to {path}")


def load_dataframe(path: str) -> pd.DataFrame:
    """
    Load a DataFrame from CSV.
    
    Args:
        path (str): Path to CSV file
    
    Returns:
        pd.DataFrame
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ File not found: {path}")
    print(f"📂 DataFrame loaded from {path}")
    return pd.read_csv(path)

def get_summary_stats(df):
    """
    Return summary statistics and grouped stats for a dataframe.
    """
    summary = df.describe()
    grouped = df.groupby("category")["value"].mean()
    return summary, grouped