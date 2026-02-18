import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

df = pd.read_csv("Bhel_stock_entire_data_history.csv")

df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')
df = df.set_index('Date')

daily_close = pd.to_numeric(df['Close'], errors='coerce')
daily_close = daily_close.dropna()

daily_close = daily_close.asfreq('D')
daily_close = daily_close.fillna(method='ffill')

model = ARIMA(daily_close, order=(5,1,0))
model_fit = model.fit()

model_fit.save("bhel_arima_model.pkl")
print("Model saved successfully.")
