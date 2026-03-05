# 📊 Trading Profit Patterns

## 📌 Executive Summary
This repository presents a **large-scale quantitative analysis of high-frequency EURUSD price data**, focusing on **pattern detection and short-term trend evaluation**.

The goal is to identify statistically significant **price patterns** using high-resolution time-series data (1-minute and 2-minute intervals) and evaluate their predictive reliability.

> **Data Acquisition & Processing:**  
> Raw EURUSD 1-minute data (2015–2021) was sourced from [Kaggle – Forex EURUSD 1m Data](https://www.kaggle.com/datasets/ankitjha420/forex-eurusd-1m-data-2015-to-2021).  
> Data was cleaned, chronologically sorted, deduplicated, and aggregated to 2-minute intervals.  
> All preprocessing was performed in Python using **vectorized operations with Pandas**, emphasizing reproducibility and computational efficiency.

---

# 🧠 Analysis Framework

## 📈 Pattern Detection

**Upward Pattern (Bullish Equivalent)**

- Current 2-min candle closes above previous high  
- Candle body dominates upper wick  
- Detection triggers evaluation of next 2-min interval outcome  

**Downward Pattern (Bearish Equivalent)**

- Current 2-min candle closes below previous low  
- Candle body dominates lower wick 
- Detection triggers evaluation of next 2-min interval outcome  

**Execution Logic:** For each detected pattern, the subsequent interval is analyzed to evaluate pattern reliability.

---

# 🖼 Pattern Visualization

### Upward Pattern Example
![Upward Pattern](patterns/upward_pattern.png)

### Downward Pattern Example
![Downward Pattern](patterns/downward_pattern.png)

> **Tip:** Images illustrate sequential behavior of price movements for visual inspection of detected patterns.

---

# ⚙️ Dataset Profile

| Metric | Value |
|--------|-------|
| Instrument | EURUSD |
| Timeframes | 1-minute & 2-minute |
| 1-min Candles | 3,165,120 |
| 2-min Candles | 1,582,560 |
| Backtest Type | Vectorized evaluation of sequential patterns |
| Data Integrity | M1 merged, cleaned, chronologically sorted, deduplicated; M2 generated from M1 |
| Environment | Python + Pandas in Visual Studio Code |

---

# 📈 Analysis Results

| Metric | Value |
|--------|-------|
| Patterns Detected | 81,938 |
| Patterns “Success” | 41,908 |
| Patterns “Failure” | 40,030 |
| Pattern Accuracy | 51.15% |

**Interpretation:**  
- High-frequency price series are **noise-dominated**  
- Short-term patterns may reflect temporary fluctuations rather than lasting trends  
- Vectorized analysis enables efficient evaluation of millions of data points  
- Reproducible workflow separates **data ingestion → preprocessing → pattern detection → evaluation**

---

# 🔎 Insights

- Patterns often **do not reliably predict next interval**, confirming importance of statistical validation  
- Workflow highlights **data cleaning, aggregation, and evaluation efficiency**  
- Modular pipeline ensures **reproducibility and scalability**  

---

# 🚀 Potential Extensions

- Pattern accuracy segmentation by time-of-day (Asia / London / NY sessions)  
- Volatility regime conditioning  
- Pattern size percentile analysis  
- Integration of higher timeframe trend filters  
- Pre-pattern range compression detection  

---

# 🛠 Tech Stack

- Python  
- Pandas (vectorized operations for high-volume data)  
- Visual Studio Code  

---

# 📌 Author Notes

This project demonstrates:

- Large-scale **data wrangling and aggregation**  
- **Rigorous statistical evaluation** of sequential patterns  
- **Workflow modularity and reproducibility**  
- Quantitative reasoning applied to high-frequency time-series data
