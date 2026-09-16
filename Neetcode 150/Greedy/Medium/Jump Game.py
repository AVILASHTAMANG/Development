# You are given an integer array nums where each element nums[i] indicates your maximum jump length at that position.
# Return true if you can reach the last index starting from index 0, or false otherwise.

from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #backward greedy approach
        # n= len(nums)
        # goal = n-1
        # for i in range(n-2,-1,-1):
        #     if (i+nums[i]) >= goal:
        #         goal = i
        # return goal==0

        #forward greedy approach
        max_reach = 0
        for i in range(len(nums)):
            if i>max_reach:
                return False
            max_reach = max(max_reach, i+nums[i])
            if max_reach>=len(nums)-1:
                return True

if __name__=='__main__':
    nums = [1,2,1,0,1]
    print(Solution().canJump(nums))