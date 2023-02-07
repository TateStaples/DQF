import math

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def func(x):
    return 1480 * math.exp(-0.000804 * x)
if __name__ == '__main__':
    data: pd.DataFrame = pd.read_csv("/Users/22staples/PycharmProjects/DQF/mid_frequency/MFT_Team/intro_project/train_intro.csv")
    change1 = (data["Stock2"] - data["Stock2_Delay"]) / data["Stock2"]


    prev = func(800)
    profit = 0
    for i in range(801, 1001):
        new = func(i)
        change = prev - new
        percent = change/prev
        prof = (percent) * 600_000
        print(prof)
        profit += prof
        prev = new
    print(profit)
    # quit()
    profit = 0
    for i in range(800):
        percent_changes = list()
        for stock_number in range(1, 5):
            stock = f"Stock{stock_number}"
            delayed = data[stock + "_Delay"][i]
            actual = data[stock][i]
            change = (actual-delayed)/actual
            percent_changes.append(abs(change))
        # percent_changes.sort()
        profit += (0.6 * percent_changes[-1] + 0.4 * percent_changes[-2]) * 1_000_000
        # profit += percent_changes[2]
    print(profit/4)
    quit()


    for i in range(1, 5):
        f, ax = plt.subplots(1)
        ax.plot(data[f"Stock{i}"])
        ax.set_ylim(ymin=0,ymax=2000)
        ax.plot()
        f.show()
        f.savefig(f"/Users/22staples/PycharmProjects/DQF/mid_frequency/stock_imgs/Stock{i}")

    print(data.head(10))

