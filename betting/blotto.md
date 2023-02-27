# Sport Betting Introduction

## Blotto
Given a battle between 100 troops, if there are 10 (weighted) control points and whoever sends the most troops to each point wins, what is the optimal troop allocation strategy

### Data Analysis

### Ideation
Given a dataset of 10,000 oppenents, how would you maximize your average points. 

Intuitively it seems that this could be solved fairly easialy by calculating the points earned per troop for all 0-100 on each fort.
(Ex. 10 troops = 50% win on fort10: 0.5 expected points per troop)

Then we can just greedily take the allocations that are highest EV (probably requires a little dynamic programming).

### Code

First we get the EVs of each allocation

```
dataset = pd.DataFrame()  # id, troop1, troop2, ... troop10
ev = [[fort * (dataset[f"troop{fort}"] < troop).mean() + fort/2 * (dataset[f"troop{fort}"] == troop).mean()
            for troop in range(0, 101)] for fort in range(1, 11)]     
```

I need more practice with dynamic programming so I just implement the greedy algorithm here. I know with more research there is a more optimal way to solve for this

```
remaining_troops = 100
allocations = [0] * len(ev)

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
        remaining_troops -= best_allocation
        print(f"allocating: {troops_used} to fort {best_fort}")  # todo: paradoxes and dynamic programming
```