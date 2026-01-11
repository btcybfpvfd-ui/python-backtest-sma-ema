import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Télécharger les données
data = yf.download("AAPL", start="2022-01-01")

# Moyennes mobiles
data["SMA20"] = data["Close"].rolling(20).mean()
data["SMA50"] = data["Close"].rolling(50).mean()

# Signaux
data["Signal"] = 0
data.loc[data["SMA20"] > data["SMA50"], "Signal"] = 1

# Backtest simple
data["Return"] = data["Close"].pct_change()
data["Strategy"] = data["Signal"].shift(1) * data["Return"]

# Résultats
equity = (1 + data[["Return", "Strategy"]]).cumprod()

equity.plot(title="SMA Strategy vs Buy & Hold")
plt.show()
