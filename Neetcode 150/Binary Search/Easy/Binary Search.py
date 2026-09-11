# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.
# Your solution must run in O(logn) time.

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low<=high:
            mid = (high + low)//2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                high = mid-1
            else:
                low = mid+1
        return -1

if __name__ == '__main__':
    nums = [3, 7, 9, 10, 11]
    target = 7
    print(Solution().search(nums,target))
