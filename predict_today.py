
import pandas as pd
import numpy as np
import joblib
import yfinance as yf


model = joblib.load("bhel_minute_model.pkl")


ticker = yf.Ticker("BHEL.NS")
data = ticker.history(period="1d", interval="5m")

if data.empty or len(data) < 2:
    raise RuntimeError("Not enough live data fetched")

latest = data.iloc[-1]
previous = data.iloc[-2]

X_today = pd.DataFrame([{
    "open":   latest['Open'],
    "high":   latest['High'],
    "low":    latest['Low'],
    "close":  latest['Close'],
    "volume": latest['Volume']
}])

predicted_return = model.predict(X_today)[0]

last_close = latest['Close']
prev_close = previous['Close']

predicted_next_close = last_close * (1 + predicted_return)
predicted_pct_move = predicted_return * 100
previous_pct_move = (last_close - prev_close) / prev_close * 100

print("Last Close               :", last_close)
print("Predicted Return         :", predicted_return)
print("Predicted Next Close     :", predicted_next_close)
print(f"Predicted % Move         : {predicted_pct_move:.4f}%")
print(f"Previous Candle % Move   : {previous_pct_move:.4f}%")

max_allowed_move = 1.0  # 1% per 5-min candle

if abs(predicted_pct_move) > max_allowed_move:
    print("⚠️ Prediction rejected (unrealistic move)")
    bias = "NO TRADE ⚖️"
else:
    threshold = 0.1  # 0.1%

    if predicted_pct_move > threshold:
        bias = "BUY 📈"
    elif predicted_pct_move < -threshold:
        bias = "SELL 📉"
    else:
        bias = "NO TRADE ⚖️"

print("Market Bias              :", bias)
