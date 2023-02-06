# IMPORTS
import random
from dataclasses import dataclass
from enum import Enum, auto
from typing import Type

from attr import dataclass

MAX_SIZE = 1000


class Side(Enum):
    buy = auto()
    sell = auto()
    notrade = auto()


@dataclass
class Market:
    bid: int = 0
    bid_size: int = 1
    ask: int = 100
    ask_size: int = 1

    def width(self) -> int:
        return self.ask - self.bid

    def better_side(self, fair) -> Type[Side]:
        return Side.buy if (self.bid-fair)*self.bid_size < (fair - self.ask) * self.ask_size else Side.sell


@dataclass
class TradeLog():
    true_value: int
    market: Type[Market]
    side: Side
    taker_contracts: int
    taker_cash: int
    maker_contracts: int
    maker_cash: int


class Game():
    def __init__(self, taker, maker) -> None:
        if not (issubclass(taker, Taker) and issubclass(maker, Maker)):
            raise Exception("Need to provide a Taker and a Maker")
        self.taker_class = taker
        self.maker_class = maker

    def runGame(self, seed=0) -> dict:
        if seed:
            random.seed(seed)
        true_value = random.randint(0, 100)
        taker = self.taker_class(true_value)
        maker = self.maker_class()
        pos = {"taker": {"contracts": 0, "cash": 0},
               "maker": {"contracts": 0, "cash": 0}}
        log = []
        for round in range(3):
            market = maker.get_market(round)
            market.bid_size = max(min(market.bid_size, MAX_SIZE), 1)
            market.ask_size = max(min(market.ask_size, MAX_SIZE), 1)

            if (market.width() > 10):
                pos["maker"]["cash"] += - 100
                market = Market(45, 1, 55, 1)

            side = taker.do_trade(market, round)

            if side == Side.notrade and market.width() <= 10:
                side = Side.buy
                pos["taker"]["cash"] += -100
            if side == Side.buy:
                cash = market.ask*market.ask_size
                pos["taker"]["contracts"] += market.ask_size
                pos["taker"]["cash"] += -cash
                pos["maker"]["contracts"] += - market.ask_size
                pos["maker"]["cash"] += cash
            elif side == Side.sell:
                cash = market.bid*market.bid_size
                pos["taker"]["contracts"] += -market.bid_size
                pos["taker"]["cash"] += cash
                pos["maker"]["contracts"] += market.bid_size
                pos["maker"]["cash"] += -cash
            elif side != Side.notrade:
                raise Exception("Invalid Side")

            maker.update_trade(side)

            log.append(TradeLog(true_value, market, side, pos["taker"]["contracts"],
                       pos["taker"]["cash"], pos["maker"]["contracts"], pos["maker"]["cash"]))

        return {"taker_pnl": pos["taker"]["cash"] + true_value*pos["taker"]["contracts"],
                "maker_pnl": pos["maker"]["cash"] + true_value*pos["maker"]["contracts"],
                "log": log}


class Taker():
    def __init__(self, true_value=50) -> None:
        self.true_value = true_value

    def do_trade(self, market: Type[Market], round: int) -> Type[Side]:
        return Side.notrade


class Maker():
    def __init__(self) -> None:
        pass

    def get_market(self, round: int) -> Market():
        return Market()

    def update_trade(self, side: Type[Side]) -> None:
        return


def test(taker, maker) -> None:
    game = Game(taker, maker)
    results = game.runGame()
    print("taker_pnl: ", results['taker_pnl'])
    print("maker_pnl: ", results['maker_pnl'])
    for log in results["log"]:
        print(log)


def main() -> int:
    test(Taker, Maker)
    return 0


if __name__ == "__main__":
    main()