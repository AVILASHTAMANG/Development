# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
#
# On each day, you may decide to buy and/or sell the stock. However, you can buy it then immediately sell it on the same
# day. Also, you are allowed to perform any number of transactions but can hold at most one share of the stock at any
# time.
#
# Find and return the maximum profit you can achieve.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #profit = 0
        # for i in range(1, len(prices)):
        #     if prices[i]>prices[i-1]:
        #         profit += prices[i] - prices[i-1]
        # return profit

        #### Dynamic Approach #####
        '''
        At the end of each day i, you can only be in one of two distinct states:
        hold: You currently own one share of the stock.
        cash: You currently own zero shares of the stock.

        1. hold[i] : max balance if you hold one share at the end of day i.
        * You already held a share yesterday and did nothing: hold[i-1]
        * You had no share yesterday and bought one today: cash[i-1] - prices[i]

        hold[i] = max(hold[i-1], cash[i-1] - prices[i])

        2. cash[i]: Your max balance if you hold zero shares at the end of day i.
        * You had no share yesterday and did nothing: cash[i-1]
        * You held a share yesterday and sold it today: hold[i-1] + prices[i]

        cash[i] = max(cash[i-1], hold[i-1] + prices[i]
        '''
        cash = 0
        hold = -prices[0]
        for price in prices[1:]:
            prev_cash = cash

            # Decide whether to keep holding or buy today
            hold = max(hold, prev_cash - price)

            # Decide whether to stay without stock or sell today
            cash = max(cash, hold + price)
        return cash


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))
