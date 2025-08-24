Project Summary

This project attempts to predict the price of a certain stock "AAPL" will go up or down on the next day. It is an extremely simple project aimed at experiencing and familirizing with a project's entire lifecycle.

Stakeholder Persona

The results of this project will be used by profolio managers, analysts and common traders. It is important in deciding whether to invest in the praticular stock or not. Therefore, they care a lot about the accuracy of the results and the relavent confidence intervals. Its correlation with other stocks or entire portfolios are not discussed in this project.

Project Structure
project-root/
│── notebooks/         # Jupyter notebooks for exploration & prototyping
│── src/               # Reusable pipeline code (cleaning, features, modeling, etc.)
│── docs/              # Documentation, stakeholder memos, visuals
│── data/              # Raw & processed datasets (not tracked in git)
│── .env               # API keys / credentials (excluded from git)
│── README.md          # Project overview

Data Storage

The folder structure for data is
data/
│── raw/               # Storage for the raw data pulled off AlphaVantage
│── processed/         # Storage for processed data

The data is stored in csv files and you can access them directly from .env using RAW_DATA and PROCESSED_DATA_..

Lifecycle Progress

This project follows a step-by-step lifecycle framework:

 Problem Framing & Scoping – Define question: Can we predict AAPL’s stock price?

 Tooling Setup – Python, Git, virtual environment, repo structure.

 Python Fundamentals – Build helper functions and utilities.

 Data Acquisition / Ingestion – Pull historical AAPL data via API.

 Data Storage – Store raw vs processed datasets.

 Data Preprocessing – Clean missing values, normalize formats.

 Outlier Analysis – Detect and cap/remove anomalies.

 Exploratory Data Analysis (EDA) – Visualize trends, seasonality, correlations.

 Feature Engineering – Create lag features, moving averages, RSI, volatility.

 Modeling – Apply regression and time-series models.

 Evaluation & Risk Communication – RMSE, MAE, directional accuracy.

 Results Reporting – Summarize insights for stakeholders.

 Productization – Package code into reusable pipeline.

 Deployment & Monitoring – Optional: API/dashboard + model drift monitoring.

 Orchestration & System Design – Plan automation (Airflow, Prefect).

