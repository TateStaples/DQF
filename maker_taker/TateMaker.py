import matplotlib.pyplot as plt

from base import *

class TateMaker(Maker):
    """
    Class to counter the Greedy Maker Strategy
    """
    def __init__(self) -> None:
        super().__init__()
        self.history = list()

    def get_market(self, round: int) -> Market():
        if round == 0:
            return Market(bid=75, ask=85)
        elif round == 1:
            if self.history[0]:  # buy
                return Market(bid=85, ask=95)
            else: # sell
                return Market(bid=65, ask=75)
        else:
            if self.history[0] != self.history[1]:
                if self.history[0]:  # buy sell
                    return Market(bid=80, bid_size=1000, ask=90, ask_size=1000)
                else:  # sell buy
                    return Market(bid=70, bid_size=1000, ask=80, ask_size=1000)
            elif self.history[0] and self.history[1]:  # buy buy
                return Market(bid=90, bid_size=1000, ask=100, ask_size=1000)

            return Market(bid=30, ask=40)  # sell sell

    def update_trade(self, side: Side) -> None:
        self.history.append(side == Side.buy)

if __name__ == '__main__':
    total = 0
    miss_total = 0
    profits = list()
    for i in range(101):
        maker = TateMaker()
        # i = 80
        round_profit = 0
        for round in range(3):
            market = maker.get_market(round)
            # print(market)
            center = market.bid + 5
            if i > center:
                maker.update_trade(Side.buy)
            else:
                maker.update_trade(Side.sell)
            miss = abs(i - center) - 5
            if i < 70: miss_total += miss
            penal = miss * -market.bid_size
            # print(i, round, market)
            round_profit += penal
        print(i, round_profit, maker.history)
        profits.append(round_profit)
        total += round_profit
        # break
    plt.plot(profits)
    plt.show()
    print(miss_total/70/3)
    print(total/101)