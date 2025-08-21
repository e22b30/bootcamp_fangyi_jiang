from typing import List, Dict
import pandas as pd
import os
import datetime as dt

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

def safe_stamp():
    return dt.datetime.now().strftime("%Y%m%d-%H%M%S")

def validate_df(df: pd.DataFrame, required_cols: List[str], dtypes_map: Dict[str, str]) -> Dict[str, str]:
    msgs = {}
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        msgs['missing_cols'] = f"Missing columns: {missing}"
    for col, dtype in dtypes_map.items():
        if col in df.columns:
            try:
                if dtype == 'datetime64[ns]':
                    pd.to_datetime(df[col])
                elif dtype == 'float':
                    pd.to_numeric(df[col])
            except Exception as e:
                msgs[f'dtype_{col}'] = f"Failed to coerce {col} to {dtype}: {e}"
    na_counts = df.isna().sum().sum()
    msgs['na_total'] = f"Total NA values: {na_counts}"
    return msgs

def safe_filename(prefix: str, meta: Dict[str, str]) -> str:
    mid = "_".join([f"{k}-{str(v).replace(' ', '-')[:20]}" for k, v in meta.items()])
    return f"{prefix}_{mid}_{safe_stamp()}.csv"