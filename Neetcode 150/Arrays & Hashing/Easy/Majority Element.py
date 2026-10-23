# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times in the array.
# You may assume that the majority element always exists in the array.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if candidate == num:
                count += 1
            else:
                count -= 1
        return candidate

if __name__ == '__main__':
    nums = [5, 5, 1, 1, 1, 5, 5]
    print(Solution().majorityElement(nums))