# Given an array of integers nums, find the subarray with the largest sum and return the sum.
# A subarray is a contiguous non-empty sequence of elements within an array.
# Kadane's algorithm
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        curr_max = global_max = nums[0]
        for num in nums[1:]:
            # Decide whether to add to the existing subarray or start a new one
            curr_max = max(num,curr_max+num)
            # Update the global maximum if the current subarray sum is larger
            global_max = max(curr_max,global_max)
        return global_max

if __name__=='__main__':
    nums = [2, -3, 4, -2, 2, 1, -1, 4]
    print(Solution().maxSubArray(nums))
