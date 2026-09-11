# You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.
# You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.
# Return the minimum integer k such that you can eat all the bananas within h hours.

from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low<high:
            mid = (low+high)//2
            hours = 0
            for pile in piles:
                hours+=(pile+mid-1)//mid
            if hours<=h:
                high=mid
            else:
                low=mid+1
        return low

if __name__ == '__main__':
    matrix = [1,11,4,3]
    target = 10
    print(Solution().minEatingSpeed(matrix, target))
