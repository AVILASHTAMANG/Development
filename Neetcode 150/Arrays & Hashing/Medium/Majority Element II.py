# You are given an integer array nums of size n, find all elements that appear more than ⌊ n/3 ⌋ times. You can return
# the result in any order.

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # freq = Counter(nums)
        # n = len(nums)
        # res = []
        # for key, value in freq.items():
        #     if value > abs(n/3):
        #         res.append(key)
        # return res

        ####Could you solve the problem in linear time and in O(1) space?####
        # Step 1: Find the top two potential candidates
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                # Triplet cancellation: discard one of each distinct element
                # if num is not equal to any of the 2 candidates
                count1 -= 1
                count2 -= 1

        # Step 2: Verify candidate frequencies
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        threshold = len(nums) // 3
        res = []

        if count1 > threshold:
            res.append(candidate1)
        if candidate2 is not None and count2 > threshold:
            res.append(candidate2)

        return res

if __name__ == '__main__':
    nums = [5, 2, 3, 2, 2, 2, 2, 5, 5, 5] # Output: [2,5]
    print(Solution().majorityElement(nums))