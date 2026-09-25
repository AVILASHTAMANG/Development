# Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.
#
# By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.
#
# Follow-up: Can you solve it without sorting?

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]

if __name__ == '__main__':
    nums = [2,3,1,1,5,5,4]
    k = 3
    print(Solution().findKthLargest(nums, k))
