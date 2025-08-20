Stakeholder Memo

Project: Predicting AAPL Stock Price Trends
Prepared by: Fangyi Jiang
Date: 08/20/2025

Executive Summary

We developed a predictive model to forecast daily stock price trends for Apple Inc. (AAPL). The model shows a meaningful ability to anticipate short-term price movements, which can support better trading strategies and risk management. Early results indicate the potential for improved decision-making compared to relying solely on historical averages or market sentiment.

Context

Apple is one of the most traded and influential stocks in global markets.

Accurate short-term price predictions could benefit portfolio managers, traders, and risk analysts by enhancing entry/exit timing.

Current methods used by our team rely on descriptive analysis and market news, which are reactive rather than predictive.

Approach

Collected 5 years of historical daily price data from Alpha Vantage.

Applied time-series modeling techniques (ARIMA and regression with lagged features).

Compared predictions against actual closing prices over the past 6 months.

Key Findings

Model reduced prediction error by ~10–15% versus a simple moving average baseline.

Accuracy was highest in stable market periods, with reduced performance during highly volatile weeks (e.g., earnings announcements).

Short-term (1–5 day horizon) predictions are more reliable than medium-term forecasts.

Recommendations

Pilot the model for AAPL trading strategy backtesting.

Integrate with existing dashboards to provide daily forecast signals.

Use predictions as a supplement, not a replacement, for human analyst judgment.

Risks & Limitations

Market shocks (macroeconomic events, earnings surprises) are difficult for the model to capture.

Predictions are probabilistic, not guaranteed — risk management protocols remain essential.

Model currently focused only on AAPL; generalizability to other tickers is untested.

Next Steps

Expand dataset to include market sentiment indicators (news, social media).

Automate daily retraining and forecast generation.

Evaluate applicability to other tech sector stocks (e.g., MSFT, AMZN).

Present results of backtesting on simulated trading strategies to quantify financial impact.