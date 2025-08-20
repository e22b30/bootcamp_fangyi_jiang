Data Handling

data_ingestion.py → functions to fetch stock data (API calls, CSV loading, etc.)

data_storage.py → functions for saving/loading data locally or in a database

Preprocessing & Cleaning

cleaning.py → missing values, outlier removal, normalization

feature_engineering.py → technical indicators (moving averages, RSI, etc.)

Modeling

model.py → train/test functions for regression, time series, ML models

evaluation.py → performance metrics, cross-validation

Utilities

config.py → central place for stock name, API keys (or read from .env)

logger.py → logging setup for monitoring pipeline runs

helpers.py → misc utility functions

Pipeline Scripts

pipeline.py → orchestrates the entire workflow (load data → clean → feature engineering → train model → evaluate)
