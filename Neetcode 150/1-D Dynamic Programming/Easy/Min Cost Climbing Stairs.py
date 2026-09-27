# You are given an array of integers cost where cost[i] is the cost of taking a step
# from the ith floor of a staircase. After paying the cost, you can step to either the (i + 1)th floor
# or the (i + 2)th floor.
#
# You may choose to start at the index 0 or the index 1 floor.
#
# Return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost.

from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # we will use Memoization method (top-down approach) i,.e,
        # While tabulation builds the answer from the ground up using a loop, memoization uses a recursive function
        # combined with a cache to compute answers backward from the destination.
        # we'll be thinking from the last element in the array

        n = len(cost)
        # Create a memoization dictionary (or array) to store already computed results
        memo = {}

        def helper(i: int) -> int:
            # Base cases: reaching index 0 or 1 costs nothing because you can start there for free
            if i <= 1:
                return 0

            # If we have already calculated the min cost for this floor, return it from the cache
            if i in memo:
                return memo[i]

            # Recurrence relation: choose the minimum of coming from 1 step back or 2 steps back
            memo[i] = min(
                helper(i - 1) + cost[i - 1],
                helper(i - 2) + cost[i - 2]
            )

            return memo[i]

        # We want to find the minimum cost to reach the top (index n)
        return helper(n)

        ################we can also use tabulation:################
        n = len(cost)
        dp = [0] * (n+1)
        # Build up the solution from step 2 to the top (n)
        for i in range(2, n + 1):
            dp[i] = min(
                dp[i - 1] + cost[i - 1],  # Coming from 1 step back
                dp[i - 2] + cost[i - 2]  # Coming from 2 steps back
            )
        return dp[n]

        ##### We can also do Space Optimization for the tabulation method###########
        n = len(cost)
        prev2 = 0  # Equivalent to dp[i-2]
        prev1 = 0  # Equivalent to dp[i-1]

        for i in range(2, n+1):
            current = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
            prev2 = prev1
            prev1 = current
        return prev1

if __name__ == '__main__':
    cost = [1,2,1,2,1,1,1]
    print(Solution().minCostClimbingStairs(cost))