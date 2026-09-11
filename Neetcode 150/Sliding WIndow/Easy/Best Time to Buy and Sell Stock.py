# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day
# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            if price<min_price:
                min_price=price
            profit = price - min_price
            if profit>max_profit:
                max_profit = profit
        return max_profit

if __name__ == '__main__':
    prices = [10, 1, 5, 6, 7, 1]
    print(Solution().maxProfit(prices))