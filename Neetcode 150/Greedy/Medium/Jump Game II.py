# You are given an array of integers nums, where nums[i] represents the maximum length of a jump towards the right from index i. For example, if you are at nums[i], you can jump to any index i + j where:
#
# j <= nums[i]
# i + j < nums.length
# You are initially positioned at nums[0].
#
# Return the minimum number of jumps to reach the last position in the array (index nums.length - 1). You may assume there is always a valid answer.

from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        steps, l, r = 0, 0, 0
        while r<len(nums)-1:
            max_reach = 0
            for i in range(l,r+1):
                max_reach = max(max_reach,i+nums[i])
            l = r+1
            r= max_reach
            steps += 1
        return steps

if __name__ == '__main__':
    nums = [2,4,1,1,1,1]
    print(Solution().jump(nums))