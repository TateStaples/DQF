import pandas as pd

dataset = pd.DataFrame()  # id, troop1, troop2, ... troop10
ev = [[fort * (dataset[f"troop{fort}"] < troop).mean() + fort/2 * (dataset[f"troop{fort}"] == troop).mean()
            for troop in range(0, 101)] for fort in range(1, 11)]

remaining_troops = 100
allocations = [0] * len(ev)
history = []
skipped = []

# greedy
while remaining_troops > 0:
    maxes = [max(ev[fort]) for fort in range(len(ev))]
    best_fort = maxes.index(max(maxes)) + 1
    best_allocation = ev[best_fort-1].index(max(ev[best_fort-1]))
    value = ev[best_fort-1][best_allocation]
    ev[best_fort - 1][best_allocation] = 0  # prevent repeats
    if best_allocation < allocations[best_fort-1]:
        continue  # ignore because already done
    troops_used = best_allocation - allocations[best_fort-1]
    if troops_used <= remaining_troops:
        history.append(())
        remaining_troops -= best_allocation
        print("allocating")  # todo: paradoxes and dynamic programming