# 📈 Stock Price Prediction Model (BHEL – NSE)

This repository contains a **machine learning–based stock prediction system** designed to predict the **next 5-minute candle return** for **BHEL (Bharat Heavy Electricals Limited)** listed on the NSE.

The project implements a complete **train → model persistence → live prediction** pipeline using historical minute-level market data and real-time data fetched from Yahoo Finance.

---

## Repository Structure


├── requirements.txt       
├── Bhel.py                 
├── predict_today.py        

---

## Technologies Used

1. Python 3.9+  
2. Pandas  
3. NumPy  
4. Scikit-learn  
5. yfinance  
6. Joblib  

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

## WorkFlow

yfinance → pandas → numpy → scikit-learn → joblib

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

Loading the saved trained model (`bhel_minute_model.pkl`)  
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

Maximum allowed price movement per 5-minute candle is ±1%  
Predictions exceeding this threshold are automatically rejected  
A minimum movement threshold helps prevent over-trading during low volatility 

---

## Installation

Install all required dependencies using:

pip install -r requirements.txt  

Please Use a virtual environment

---

## Disclaimer

This project is intended strictly for **educational and research purposes**.  
It does **not constitute financial or investment advice**.  
Do not use this system for live trading without extensive backtesting and proper risk management.  
The author is not responsible for any financial losses incurred.

---

## Future Improvements

Deploy as a dashboard
Introduce Model Monitoring
Graphical Representation of the Current and Next stock close price
Add multiple stocks


---

## Support

If you find this project useful, please give it a ⭐ on GitHub.
