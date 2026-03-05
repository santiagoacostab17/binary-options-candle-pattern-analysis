import pandas as pd

print("\n===== START BACKTEST =====")

# Load data
df1 = pd.read_csv("EURUSD_1m_clean.csv")
df2 = pd.read_csv("EURUSD_2m_clean.csv")

# Candle structure
df2["top_wick"] = df2.high - df2[["open","close"]].max(axis=1)
df2["bot_wick"] = df2[["open","close"]].min(axis=1) - df2.low
df2["body"] = (df2.close - df2.open).abs()

# Patterns
bull = (df2.close > df2.open) & (df2.top_wick < df2.body) & (df2.close > df2.high.shift(1))
bear = (df2.close < df2.open) & (df2.bot_wick < df2.body) & (df2.close < df2.low.shift(1))

wins = losses = trades = 0

for i in range(1, len(df2)-1):

    m1 = (i+1)*2
    if m1 >= len(df1):
        break

    entry = df2.open[i]
    next_close = df2.close[i+1]

    if bull[i] and df1.low[m1] <= entry:
        trades += 1
        wins += next_close >= entry
        losses += next_close < entry

    elif bear[i] and df1.high[m1] >= entry:
        trades += 1
        wins += next_close <= entry
        losses += next_close > entry

winrate = wins / trades if trades else 0

print("\nResults")
print("Wins:", wins)
print("Losses:", losses)
print("Trades:", trades)
print("Winrate:", round(winrate*100,2), "%")

print("\n===== END BACKTEST =====")
