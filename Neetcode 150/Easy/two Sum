class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_arr={}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_arr:
                return [num_arr[complement],i]
            num_arr[num] = i 
