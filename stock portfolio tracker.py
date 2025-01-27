import yfinance as yf
import pandas as pd

class SimpleStockPortfolio:
    def __init__(self):
        self.portfolio = pd.DataFrame(columns=["Symbol", "Shares", "Price", "Value"])

    def add_stock(self, symbol, shares):
        stock = yf.Ticker(symbol)
        price = stock.history(period='1d')['Close'][0]
        value = price * shares
        self.portfolio = pd.concat([self.portfolio, pd.DataFrame({"Symbol": [symbol], "Shares": [shares], "Price": [price], "Value": [value]})], ignore_index=True)
        print(f"Added {shares} shares of {symbol} at ${price:.2f}")

    def remove_stock(self, symbol):
        self.portfolio = self.portfolio[self.portfolio['Symbol'] != symbol]
        print(f"Removed {symbol} from portfolio")

    def update_prices(self):
        for index, row in self.portfolio.iterrows():
            stock = yf.Ticker(row["Symbol"])
            price = stock.history(period='1d')['Close'][0]
            self.portfolio.at[index, "Price"] = price
            self.portfolio.at[index, "Value"] = price * row["Shares"]

    def show_portfolio(self):
        self.update_prices()
        print(self.portfolio)
        total_value = self.portfolio["Value"].sum()
        print(f"Total Portfolio Value: ${total_value:.2f}")

# Example usage:
portfolio = SimpleStockPortfolio()
portfolio.add_stock("AAPL", 10)
portfolio.add_stock("GOOGL", 5)
portfolio.show_portfolio()
portfolio.remove_stock("AAPL")
portfolio.show_portfolio()
