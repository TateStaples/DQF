from trader_class import Trader
from pandas import pd

class TateTrader(Trader):
    def __init__(self):
        super().__init__()
        data: pd.DataFrame = pd.read_csv("/mid_frequency/MFT_Team/intro_project/train_intro.csv")
        self.history = data["Stock1"]
    def MakeTrades(self, time, stock_prices):
        # stock1 is the most linear - just linear model
        # stock2 noisy flat - combined knowledge and forward predictions
        # stock3 mostly just flat - idk how to profit from this
        # stock4 is most volatile - only trade with info
        trades = {"Stock1": -1e10,"Stock2": 0,"Stock3": 0,"Stock4": 0,}
        self.history.append(stock_prices["Stock1"])
        if self.history[-10:].mean() > 0:
            trades["Stock1"] = 0
        return trades