# You are given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
# whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
#
# A subarray is a contiguous non-empty sequence of elements within an array.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        n = len(nums)
        total = 0
        min_len = float('inf')
        for end in range(n):
            total+=nums[end]
            while total>=target:
                min_len  = min(min_len, end-start+1)
                total-=nums[start]
                start+=1
        return min_len if min_len!=float('inf') else 0

if __name__=='__main__':
    target = 10
    nums = [2, 1, 5, 1, 5, 3]
    print(Solution().minSubArrayLen(target,nums))
