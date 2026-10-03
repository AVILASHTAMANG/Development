# You are given a list of non-negative integers nums, arrange them such that they form the largest number
# and return it.
#
# Since the result may be very large, so you need to return a string instead of an integer.

from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        n = len(nums)
        # bubble sort : in the below use case it will place the largest element at tjhe start after sorting the whole list
        for i in range(n):
            for j in range(n-i-1):
                if nums[j] + nums[j+1] < nums[j+1] + nums[j]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        if nums[0] == "0":
            return "0"
        return ''.join(nums)

if __name__ == '__main__':
    nums = [3, 30, 34, 5, 9]
    print(Solution().largestNumber(nums))