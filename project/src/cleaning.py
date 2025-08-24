# Imports
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import missingno as msno

## function to fill missing value as the median of the column
def fill_missing_median(df, columns=None):
    df_copy = df.copy()
    if columns is None:
        columns = df.select_dtypes(include=np.number).columns
    for col in columns:
        df_copy[col] = df_copy[col].fillna(df_copy[col].median())
    return df_copy
## function to drop the missing value
def drop_missing(df, columns=None, threshold=None):
    df_copy = df.copy()
    if columns is not None:
        return df_copy.dropna(subset=columns)
    if threshold is not None:
        return df_copy.dropna(thresh=int(threshold*df_copy.shape[1]))
    return df_copy.dropna()
## function to normalize the data
def normalize_data(df, columns=None, method='minmax'):
    df_copy = df.copy()
    if columns is None:
        columns = df_copy.select_dtypes(include=np.number).columns
    if method=='minmax':
        scaler = MinMaxScaler()
    else:
        scaler = StandardScaler()
    df_copy[columns] = scaler.fit_transform(df_copy[columns])
    return df_copy
## function to handle duplicate entries
def drop_duplicate(df):
    df_copy = df.copy()
    df_copy = df_copy.drop_duplicates(subset=['date'], keep='last')
    return df_copy
## function to fill the missing value as the mean of the previous and next extry
def fill_missing_with_mean(df, col):
    df_copy = df.copy()
    series = df[col].copy()
    
    for idx in series[series.isna()].index:
        prev_val = series.loc[:idx].ffill().iloc[-2] if idx > series.index.min() else np.nan
        next_val = series.loc[idx:].bfill().iloc[0] if idx < series.index.max() else np.nan
        
        if not np.isnan(prev_val) and not np.isnan(next_val):
            series.loc[idx] = (prev_val + next_val) / 2
        elif not np.isnan(prev_val):  # only prev available
            series.loc[idx] = prev_val
        elif not np.isnan(next_val):  # only next available
            series.loc[idx] = next_val
    
    df_copy[col] = series
    return df_copy