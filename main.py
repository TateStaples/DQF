import matplotlib.pyplot as plt
import numpy as np

print(2 * 10 * 2 * 10)
quit()
profit = np.zeros(101)

for dollars in range(101):
    spread1 = 50
    prof1 = dollars - (spread1 + 5) if dollars < spread1 else (spread1 - 5) - dollars
    spread2 = 25 if dollars > spread1 else 75
    prof2 = dollars - (spread2 + 5) if dollars > spread2 else (spread2 - 5) - dollars
    spread3 = spread2 + 12.5 if spread2 < dollars else spread2 - 12.5
    prof3 = dollars - (spread3 + 5) if dollars > spread3 else (spread3 - 5) - dollars
    profit[dollars] = prof1 + prof2 + prof3
    print(dollars, profit[dollars], spread1, spread2, spread3)

plt.plot(profit)
print(profit.mean())
plt.show()
