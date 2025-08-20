## Stage 6: Data Preprocessing

In this stage, we use functions imported from cleaning.py to perform cleaning operations to existing data.

First we fill the missing numeric values with the median of the column.
We then drop the rows with any missing values left.
Finally, we normalize the data for better analysis.

It's important to keep in mind that the second and third steps cannot be filpped as it would drop all missing numeric values and lead to less data for analysis.
