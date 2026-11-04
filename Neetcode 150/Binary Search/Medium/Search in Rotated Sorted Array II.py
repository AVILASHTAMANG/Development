# You are given an array of length n which was originally sorted in non-decreasing order (not necessarily with distinct
# values). It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:
#
# [3,4,5,6,1,2] if it was rotated 4 times.
# [1,2,3,4,5,6] if it was rotated 6 times.
# Given the rotated sorted array nums and an integer target, return true if target is in nums, or false if it is not
# present.
#
# You must decrease the overall operation steps as much as possible.

class Solution:
    def search(self, nums: List[int], target: int) -> bool:

if __name__=='__main__':
    nums = [3, 4, 4, 5, 6, 1, 2, 2]
    target = 1
    print(Solution().search(nums,target))
