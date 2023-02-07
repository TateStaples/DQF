# Description
Analyze the 800 time-steps of following 4 stocks and devise an algorithm to trade the next 200 time-steps.
### Stock1
Linear, low noise fall

![Img of Stock1 price in same data](/Users/22staples/PycharmProjects/DQF/mid_frequency/stock_imgs/Stock1.png "Stock1 valuation")

### Stock2
Slight trends, moderate noise

![Img of Stock2 price in same data](/Users/22staples/PycharmProjects/DQF/mid_frequency/stock_imgs/Stock2.png "Stock2 valuation")

### Stock3
Low noise, flat

![Img of Stock3 price in same data](/Users/22staples/PycharmProjects/DQF/mid_frequency/stock_imgs/Stock3.png "Stock3 valuation")

### Stock4
Few trends, highly volatile

![Img of Stock4 price in same data](/Users/22staples/PycharmProjects/DQF/mid_frequency/stock_imgs/Stock4.png "Stock4 valuation")

## Questions

### What is your strategy? 
Without having the non-delayed information, I think the safest and most consistent rewards would come from selling Stock1.
It has a very predictable trend with little exposure to variance. I do use a rolling average to check for change in trends and stop selling if the previous 10 window is positive.

Stock3 is mostly flat so there is a lot of money to be made, Stock4 is too volatile to generate effective trends, and Stock2 just doesn't have the level of change as Stock1.
### How much do you expect to make? Justify with a statistical model.
I modeled Stock1 with a exponential fit. That gave the following equation:

```math
 price(t) = 1480 * e^(-0.000804t)
```

Assuming the model is met, we should make ~$100,000 over the next 200 time steps.


### How much is non-delayed data worth?
From the given 800 time-steps, the average max profit per timestep is ~3.5%. 
Given our max investment of $1,000,000 this means we can profit $5000 on average per round.
Over 200 rounds, this gives $7,000,000 in expected profit.

This valuation is limited by the opportunity cost of the profits we would have made with just our own prediction models. 
In the last section we determined that the expected value was $100,000. Therefore it is work 7,900,000 to have non-delayed data.
