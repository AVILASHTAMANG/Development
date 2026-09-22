# You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.
# There is exactly one repeated integer in nums, and every other integer appears at most once.
# Return the repeated integer.

from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Flyod's Tortoise & Hare algorithm for cycle detection.
        # Treat the list as an implicit linked list: from index i , follow the "pointer" nums[i]
        # Since there are n+1 nodes but only n possible values, a cycle must exist -- and the cycles's entrance is the duplicate

        # Find the meeting point inside the cycle
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow] # 1 step
            fast = nums[nums[fast]] # 2 step
            if slow == fast:
                break

        # Find the entrance of the cycle which is the duplicate
        slow = nums[0]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

if __name__ == '__main__':
    nums = [1,3,4,2,2]
    print(Solution().findDuplicate(nums))
