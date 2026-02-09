# 📈 Stock Price Prediction Model (BHEL – NSE)

This repository contains a **machine learning–based stock prediction system** designed to predict the **next 5-minute candle return** for **BHEL (Bharat Heavy Electricals Limited)** listed on the NSE.

The project implements a complete **train → model persistence → live prediction** pipeline using historical minute-level market data and real-time data fetched from Yahoo Finance.

---

## Repository Structure

.
├── requirements.txt      # Python dependencies  
├── Bhel.py               # Model training and evaluation  
├── predict_today.py      # Live market prediction script  

---

## Technologies Used

Python 3.9+  
Pandas  
NumPy  
Scikit-learn  
yfinance  
Joblib  

---

## Model Description

Algorithm: Random Forest Regressor  
Objective: Predict the return of the next 5-minute candle  

Target Formula:  
next_return = (next_close - current_close) / current_close  

Input Features:  
Open  
High  
Low  
Close  
Volume  

Timeframe:  
Training: Historical 5-minute candles  
Prediction: Latest live 5-minute candle  

---

## Model Training (Bhel.py)

The training script performs the following steps:

Loads historical NSE minute-level stock data  
Cleans and converts numeric columns  
Sorts data by timestamp to prevent data leakage  
Engineers the next candle return as the prediction target  
Splits data using a time-based 80/20 train-test split  
Trains a Random Forest regression model  
Evaluates performance using MAE, RMSE, and R² score  
Performs a sanity check on the most recent candle  
Saves the trained model as `bhel_minute_model.pkl`  

Command to train the model:

python Bhel.py

---

## Live Prediction (predict_today.py)

The live prediction script performs real-time inference by:

Loading the trained model (`bhel_minute_model.pkl`)  
Fetching live 5-minute market data for BHEL.NS  
Predicting the next candle return and next close price  
Calculating percentage price movement  
Applying sanity and risk filters  
Generating a market bias signal (BUY / SELL / NO TRADE)  

Command to run live prediction:

python predict_today.py

Sample Output:

Last Close               : 268.0  
Predicted Return         : 0.0012  
Predicted Next Close     : 268.32  
Predicted % Move         : 0.1200%  
Previous Candle % Move   : 0.2244%  
Market Bias              : BUY 📈  

---

## Risk Management

Maximum allowed price movement per 5-minute candle: ±1%  
Predictions exceeding this threshold are automatically rejected  
A minimum movement threshold helps prevent over-trading during low volatility  

---

## Installation

Install all required dependencies using:

pip install -r requirements.txt  

Using a virtual environment is strongly recommended.

---

## Disclaimer

This project is intended strictly for **educational and research purposes**.  
It does **not constitute financial or investment advice**.  
Do not use this system for live trading without extensive backtesting and proper risk management.  
The author is not responsible for any financial losses incurred.

---

## Future Improvements

Add technical indicators (RSI, EMA, MACD, VWAP)  
Implement a backtesting framework  
Support multiple stocks  
Enhance feature engineering  
Deploy as an API or dashboard  
Introduce model monitoring and versioning  

---

## Contributing

Contributions are welcome.  
Fork the repository, create a feature branch, and submit a pull request.

---

## Support

If you find this project useful, consider giving it a ⭐ on GitHub.
