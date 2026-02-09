
import pandas as pd
import numpy as np
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("BHEL__EQ__NSE__NSE__MINUTE.csv")

numeric_cols = ['open', 'high', 'low', 'close', 'volume']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

df = df.sort_values('timestamp').reset_index(drop=True)

df['next_return'] = (df['close'].shift(-1) - df['close']) / df['close']

df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

X = df[['open', 'high', 'low', 'close', 'volume']]
y = df['next_return']

split_index = int(len(df) * 0.8)

X_train = X.iloc[:split_index]
X_test  = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test  = y.iloc[split_index:]

model = RandomForestRegressor(
    n_estimators=200,
    max_depth=8,
    min_samples_leaf=20,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("MAE (return) :", mean_absolute_error(y_test, predictions))
print("RMSE(return) :", np.sqrt(mean_squared_error(y_test, predictions)))
print("R2           :", r2_score(y_test, predictions))

last_features = X.iloc[[-1]]
predicted_return = model.predict(last_features)[0]

last_close = df['close'].iloc[-1]
prev_close = df['close'].iloc[-2]

predicted_next_close = last_close * (1 + predicted_return)
predicted_pct_move = predicted_return * 100
previous_pct_move = (last_close - prev_close) / prev_close * 100

print("\nLast Close               :", last_close)
print("Predicted Return         :", predicted_return)
print("Predicted Next Close     :", predicted_next_close)
print(f"Predicted % Move         : {predicted_pct_move:.4f}%")
print(f"Previous Candle % Move   : {previous_pct_move:.4f}%")

joblib.dump(model, "bhel_minute_model.pkl")
print("\nModel saved as bhel_minute_model.pkl")
