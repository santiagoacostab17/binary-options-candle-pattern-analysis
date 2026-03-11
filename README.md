# 📊 EURUSD Microstructure Pattern Backtest

## 📌 Overview
**Python-based quantitative backtesting project** analyzing high-frequency EURUSD price data.

This project evaluates a **microstructure price action pattern** using **1-minute and 2-minute candle data**, testing whether specific candle formations produce statistically consistent short-term outcomes.

The workflow demonstrates **data cleaning, time-series aggregation, vectorized numerical analysis, and reproducible quantitative workflows** applied to large financial datasets.

---

# ⚙️ Workflow

## 1️⃣ System Recognition

**Domain:** High-frequency Forex data analysis  

**Objective:**  
Evaluate whether specific **2-minute candle structures** produce a statistically meaningful directional bias in the following candle.

**Constraints**

- Large dataset (millions of rows)
- Need for efficient numerical computation
- Reproducible quantitative methodology

---

## 2️⃣ Data Collection

Source dataset:

https://www.kaggle.com/datasets/ankitjha420/forex-eurusd-1m-data-2015-to-2021

The dataset contains:

**EURUSD 1-minute OHLC candles (2015–2021)**

This allows reconstruction of higher timeframe candles while preserving **microstructure precision**.

---

## 3️⃣ Data Cleaning

Raw CSV files were processed using **pandas** to create a consistent dataset.

Cleaning pipeline steps:

- Merge multiple CSV files
- Remove unnecessary columns
- Standardize column names
- Parse datetime values
- Remove duplicate timestamps
- Sort data chronologically
- Export cleaned dataset
- Generate aggregated 2-minute candles

Outputs generated:

```
EURUSD_1m_clean.csv
EURUSD_2m_clean.csv
```

---

## 4️⃣ Pattern Detection

The strategy identifies **momentum candles with limited wick retracement**.

For each **2-minute candle**, the algorithm evaluates the following conditions.

### Bullish Pattern

```
close > open
upper_wick < body
close > previous_high
```

### Bearish Pattern

```
close < open
lower_wick < body
close < previous_low
```

If a signal occurs, the algorithm checks whether price **retraces to the candle open** using **1-minute data**.

This simulates a **limit order entry placed at the candle open price**.

Trade outcomes are evaluated using the **close of the following 2-minute candle**.

---

## 5️⃣ Backtesting Engine

The strategy is evaluated using a **NumPy-based backtesting engine** designed for high performance.

Key characteristics:

- NumPy vectorized calculations
- Minimal Python loops
- Memory-efficient array operations
- Fast processing of large time-series datasets

The backtest automatically generates a statistical report saved to:

```
backtest_results.txt
```

---

## 6️⃣ Results

Backtest results using the full dataset:

| Metric | Value |
|------|------|
| Trades | 81,938 |
| Wins | 41,908 |
| Losses | 40,030 |
| Win Rate | 51.15% |
| Profit Factor | 1.047 |
| Expectancy | 0.0229 |
| Avg Win | 1 |
| Avg Loss | -1 |
| Max Win | 1 |
| Max Loss | -1 |
| Std Deviation | 0.9997 |

---

## 📈 Interpretation

Key observations from the simulation:

- The strategy produces **near-random outcomes with a small positive bias**
- Profit factor above **1.0** suggests a **slight statistical edge**
- Expectancy is **small but positive**, which is common in microstructure strategies
- Variance is relatively high compared to the average trade outcome

Possible improvements for future research:

- Volatility filters
- Session-based filtering (London / New York)
- Spread and transaction cost modeling
- Multi-candle confirmation signals
- Risk management optimization

---

# 🚀 Key Features

| Feature | Technique |
|------|------|
| High-frequency analysis | 1-minute and 2-minute EURUSD candles |
| Pattern recognition | Candle structure analysis |
| Numerical performance | NumPy vectorized computation |
| Data engineering | Pandas preprocessing pipeline |
| Strategy evaluation | Custom backtesting engine |
| Reproducibility | Structured workflow and datasets |

---

# 🛠️ How to Run

### 1️⃣ Download the dataset

Download the EURUSD dataset from Kaggle.

### 2️⃣ Place raw files

Place the raw CSV files inside the `data` folder.

### 3️⃣ Run the cleaning pipeline

This script merges and cleans the raw data and generates the final datasets.

### 4️⃣ Run the backtest

Execute the NumPy backtesting script.

Example:

```
python backtest_numpy.py
```

Outputs generated:

```
EURUSD_1m_clean.csv
EURUSD_2m_clean.csv
backtest_results.txt
```



The workflow shows how raw financial data can be transformed into a **reproducible quantitative research pipeline using Python**.

Such pipelines are commonly used in **algorithmic trading research, financial data science, and quantitative analysis workflows**.
