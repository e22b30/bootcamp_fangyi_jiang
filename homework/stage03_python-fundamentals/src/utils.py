import pandas as pd
def get_summary_stats(df):
    """
    Return summary statistics and grouped stats for a dataframe.
    """
    summary = df.describe()
    grouped = df.groupby("category")["value"].mean()
    return summary, grouped