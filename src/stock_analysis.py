import yfinance as yf
import pandas as pd
import numpy as np

class StockAnalyzer:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.data = yf.download(ticker, start_date, end_date)
        self.returns = self.data['Adj Close'].pct_change()
    
    def calculate_volatility(self):
        return np.std(self.returns) * np.sqrt(252)  # Annualized
    
    def calculate_sharpe_ratio(self, risk_free_rate=0.04):
        excess_returns = self.returns - risk_free_rate/252
        return np.sqrt(252) * np.mean(excess_returns) / np.std(excess_returns)

    def plot_price_trend(self):
        return self.data['Adj Close'].plot(title=f'{self.ticker} Price Trend')

    def compare_with(self, other_ticker):
        other = yf.download(other_ticker, self.data.index[0], self.data.index[-1])
        return pd.DataFrame({
            self.ticker: self.data['Adj Close']/self.data['Adj Close'][0],
            other_ticker: other['Adj Close']/other['Adj Close'][0]
        }).plot(title='Normalized Price Comparison')