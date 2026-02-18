from statsmodels.tsa.arima.model import ARIMAResults

loaded_model = ARIMAResults.load("bhel_arima_model.pkl")

next_day_prediction = loaded_model.forecast(steps=1)

print("Next Day Closing Price Prediction:")
print(round(next_day_prediction.iloc[0], 2))
