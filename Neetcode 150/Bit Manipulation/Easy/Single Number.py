# You are given a non-empty array of integers nums. Every integer appears twice except for one.
# Return the integer that appears only once.
# You must implement a solution with O(n) runtime complexity and use only O(1) extra space.

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res^=i
        return res

if __name__ == '__main__':
    nums = [3,2,3]
    print(Solution().singleNumber(nums))
