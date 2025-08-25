Stage 07 – Outliers & Risk Assumptions
🎯 Goal

Learn how to detect outliers and check key statistical assumptions that affect the reliability of regression models.

🔑 Key Concepts

Outliers

Extreme values that can distort analysis.

Detection methods: Boxplot, Z-scores, IQR.

Decision: remove, transform, or keep (depending on context).

Normality

Assumes residuals follow a normal distribution.

Tools: histograms, Q-Q plots, Shapiro-Wilk test.

Homoscedasticity (Equal Variance)

Residuals should have constant spread across predictions.

Checked with residual plots.

Autocorrelation

Residuals should be independent (no patterns over time).

Commonly tested with Durbin-Watson statistic.

Risk of Assumption Violations

Biased coefficients.

Incorrect p-values and confidence intervals.

Misleading model performance metrics.

📊 Workflow

Detect Outliers

import numpy as np
z_scores = np.abs((df["col"] - df["col"].mean()) / df["col"].std())
outliers = df[z_scores > 3]


Check Normality

Plot histogram / Q-Q plot.

Apply scipy.stats.shapiro(df["col"]).

Check Homoscedasticity

Residuals vs. fitted values plot.

Check Autocorrelation

from statsmodels.stats.stattools import durbin_watson
durbin_watson(model.resid)


Communicate Risks

Document whether assumptions are met.

Explain how violations might affect decisions.

✅ Deliverables

Outlier detection and handling function(s).

Diagnostic plots (normality, residuals, autocorrelation).

Written interpretation of results and risks.