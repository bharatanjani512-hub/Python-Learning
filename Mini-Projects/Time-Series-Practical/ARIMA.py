# ==============================
# ARIMA Time Series Practical
# ==============================

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA


# Step 1: Data
data = [141, 313, 84, 225, 130, 99, 51, 103, 155, 309, 359, 240, 267, 93, 211]
series = pd.Series(data)


# Step 2: Plot Original Data
plt.plot(series)
plt.title("Original Data")
plt.show()


# Step 3: ADF Test
result = adfuller(series)
print("\nADF Statistic:", result[0])
print("p-value:", result[1])


# Step 4: Differencing
diff_series = series.diff().dropna()

plt.plot(diff_series)
plt.title("Differenced Data")
plt.show()

result2 = adfuller(diff_series)
print("\nAfter Differencing p-value:", result2[1])


# Step 5: Apply ARIMA Model
model = ARIMA(series, order=(1, 1, 1))
model_fit = model.fit()

print("\nModel Summary:\n")
print(model_fit.summary())


# Step 6: Forecast
forecast = model_fit.forecast(steps=5)

print("\nForecasted Values:")
print(forecast)