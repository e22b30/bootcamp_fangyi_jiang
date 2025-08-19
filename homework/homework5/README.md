Data Storage

This project follows a reproducible storage layer for datasets, using environment-driven paths and standard formats.

Folder Structure

data/raw/ — original, unmodified data saved as CSV

data/processed/ — cleaned or transformed data saved as Parquet

Both folders are created automatically by the utility functions if they don’t exist.

Formats

CSV (Comma-Separated Values)

Human-readable and portable

Used for storing raw snapshots of data

Parquet (columnar storage format)

Efficient for large datasets

Preserves dtypes and supports fast reads/writes

Used for processed datasets where performance matters

Environment Variables

Paths are set in the .env file to ensure reproducibility across machines:

DATA_DIR_RAW=data/raw
DATA_DIR_PROCESSED=data/processed


Code reads these values using os.getenv to determine where files are saved/loaded.

Utilities

The notebook includes reusable helpers:

write_df(df, path) → Saves DataFrame as CSV or Parquet depending on suffix

read_df(path) → Loads DataFrame automatically from CSV or Parquet

validate_loaded(original, reloaded) → Confirms shape and key column dtypes match after reload

Example Workflow

Save a DataFrame to both CSV (data/raw/) and Parquet (data/processed/).

Reload both versions and validate integrity.

Reuse write_df / read_df utilities for future datasets.
