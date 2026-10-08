# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
#
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
#
# Return the answer with the smaller index first.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_arr={}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_arr:
                return [num_arr[complement],i]
            num_arr[num] = i

if __name__ == '__main__':
    nums = [3, 4, 5, 6]
    target = 7
    print(Solution().twoSum(nums,target))
