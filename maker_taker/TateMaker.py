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
            return Market(bid=70, ask=80)
        elif round == 1:
            if self.history[0]:
                return Market(bid=80, ask=90)
            else:
                return Market(bid=60, ask=70)
        else:
            if self.history[0] != self.history[1]:
                if self.history[0]:
                    return Market(bid=75, bid_size=1000, ask=85, ask_size=1000)
                else:
                    return Market(bid=65, bid_size=1000, ask=75, ask_size=1000)
            elif self.history[0] and self.history[1]:
                return Market(bid=90, bid_size=1000, ask=100, ask_size=1000)

        return Market(bid=28, ask=38)

    def update_trade(self, side: Type[Side]) -> None:
        self.history.append(side == Side.buy)