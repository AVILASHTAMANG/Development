# You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.
#
# Return the number of distinct ways to climb to the top of the staircase.

class Solution:
    def climbStairs(self, n: int) -> int:
        # Handle the smallest base cases immediately to prevent errors
        if n <= 2:
            return n
    #
    #     # Create an array of size n+1 to store our tabulated answers.
    #     # (We use n+1 so the index numbers match the step numbers).
    #     # we usually use dp array for Tabulation method(bottom-up approach). Just a name though
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2

    # Now, imagine you want to reach step 4. Think only about your very last move. Because you can only climb 1 or 2 steps at a time, you must have arrived at step 4 from one of two places:
    # From Step 3: You took a 1-step jump to finish.
    # From Step 2: You took a 2-step jump to finish.
    # This is the secret to the whole problem: The total number of ways to reach step 4 is simply the total ways to reach step 3, PLUS the total ways to reach step 2.
    # Ways to reach step 4 = Ways to reach step 3 (which is 3) + Ways to reach step 2 (which is 2) = 5 ways.
    # Ways to reach step 5 = Ways(4) + Ways(3) = 5 + 3 = 8 ways.

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

if __name__=='__main__':
    n = 3
    print(Solution().climbStairs(n))