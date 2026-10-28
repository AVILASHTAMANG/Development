# You are given an integer array nums and an integer k, return true if there are two distinct indices i and j in the
# array such that nums[i] == nums[j] and abs(i - j) <= k, otherwise return false.

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # O(n2)
        # for i in range(len(nums) - 1):
        #     for j in range(i+1, len(nums)):
        #         if nums[j] == nums[i] and abs(i-j)<=k:
        #             return True
        # return False
        seen = {}
        for i , num in enumerate(nums):
            if num in seen and i-seen[num]<=k:
                return True
            else:
                seen[num]=i
        return False

if __name__=='__main__':
    # nums = [1, 2, 3, 1]
    # k = 3
    # nums = [2, 1, 2]
    # k = 1
    nums = [1, 0, 1, 1]
    k = 1
    print(Solution().containsNearbyDuplicate(nums, k))