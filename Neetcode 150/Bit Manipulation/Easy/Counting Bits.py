# Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].
# Return an array output where output[i] is the number of 1's in the binary representation of i.

from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1
        for i in range(1,n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1+dp[i-offset]
        return dp

if __name__=='__main__':
    n = 4
    print(Solution().countBits(n))