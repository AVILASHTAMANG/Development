# You are given an integer array nums sorted in non-decreasing order. Your task is to remove duplicates from nums in-place
# so that each element appears only once.
#
# After removing the duplicates, return the number of unique elements, denoted as k, such that the first k elements of
# nums contain the unique elements.
#
# Note:
# The order of the unique elements should remain the same as in the original array.
# It is not necessary to consider elements beyond the first k positions of the array.
# To be accepted, the first k elements of nums must contain all the unique elements.

# Return k as the final result.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        c = 0
        for i in range(1, len(nums)):
            if nums[c] != nums[i]:
                c+=1
                nums[c]=nums[i]
        return c+1

if __name__ == '__main__':
    nums = [2, 10, 10, 30, 30, 30]
    print(Solution().removeDuplicates(nums))