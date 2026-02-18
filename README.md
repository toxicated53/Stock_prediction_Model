# 📈 Stock Price Forecasting – BHEL (NSE)

A time-series forecasting project that predicts the **next trading day’s closing price** of **BHEL (Bharat Heavy Electricals Limited)** listed on the National Stock Exchange (NSE) using an **ARIMA model**.

This project demonstrates a complete workflow including:

- Historical data preprocessing  
- Time-series modeling  
- Forecast generation  
- Model persistence  
- Live inference using real-time market data  

> ⚠️ This project is built strictly for educational and research purposes.

---

## 📂 Repository Structure

```
├── requirements.txt
├── Bhel.py                # Model training script
├── predict_next_day.py       # Live prediction script
├── bhel_minute_model.pkl  # Saved trained model (generated after training)
```

---

## 🛠 Tech Stack

- Python 3.9+
- pandas
- numpy
- statsmodels
- yfinance

---

## 📊 Model Overview

**Algorithm Used:** ARIMA (AutoRegressive Integrated Moving Average)  
**Model Order:** ARIMA(5,1,0)

The model forecasts the next day's closing price using historical daily closing prices.

### Forecast Objective

The system predicts:

Next Day Closing Price

For live inference, it also calculates:

Predicted Return = (Predicted Close - Current Close) / Current Close

---

## 🔄 Workflow

### 1️⃣ Data Ingestion
- Load historical CSV stock data
- Fetch live market data via yfinance

### 2️⃣ Data Processing
- Convert `Date` column to datetime format
- Sort data chronologically (prevents data leakage)
- Handle missing values
- Resample to daily frequency
- Convert numeric columns properly

### 3️⃣ Model Training
- Fit ARIMA(5,1,0) on historical closing prices
- Perform sanity validation
- Save trained model as `.pkl` file

### 4️⃣ Live Prediction
- Load trained model
- Fetch latest market data
- Forecast next closing price
- Calculate predicted return & % movement
- Generate market bias signal (BUY / SELL / NO TRADE)

---

## 🚀 Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/Stock_prediction_Model.git
cd Stock_prediction_Model
```

### 2️⃣ Create Virtual Environment (Recommended)

Windows:
```
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:
```
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Train the Model

Run:

```
python Bhel.py
```

This will:
- Train the ARIMA model
- Save the trained model as `bhel_minute_model.pkl`

---

## 📡 Run Live Prediction

```
python predict_next_day.py
```

### Sample Output

```
Last Close               : 268.00
Predicted Return         : 0.0012
Predicted Next Close     : 268.32
Predicted % Move         : 0.1200%
Previous Candle % Move   : 0.2244%
Market Bias              : BUY 📈
```

---

## ⚖️ Risk Management

- Filters out extreme predictions beyond threshold
- Applies minimum volatility condition
- Helps prevent over-trading during low movement periods

---

## 📌 Key Concepts Demonstrated

- Time-Series Forecasting (ARIMA)
- Financial Data Preprocessing
- Chronological Data Handling
- Model Serialization using Pickle
- Real-Time Market Data Integration
- Structured ML Pipeline Design

---

## 🚧 Future Improvements

- Deploy as a Streamlit dashboard
- Add visualization for predicted vs actual prices
- Introduce rolling backtesting
- Support multiple NSE stocks
- Add automated model retraining

---

## ⚠️ Disclaimer

This project is strictly for **educational and research purposes**.

It does **not** constitute financial advice or investment recommendations.  
Do not use this system for live trading without extensive backtesting and proper risk management.  
The author assumes no responsibility for financial losses incurred.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
``
