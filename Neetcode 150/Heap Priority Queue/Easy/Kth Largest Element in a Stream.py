# Design a class to find the kth largest integer in a stream of values, including duplicates.
# E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.
#
# Implement the following methods:
#
# constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
# int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.

from typing import List
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums

        # Turn the list into a valid min-heap in O(N) time
        heapq.heapify(self.heap)

        # If we start with more than k elements, trim down to size k
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

if __name__ == '__main__':
    kthLargest = KthLargest(3, [1, 2, 3, 3])
    print(kthLargest.add(3))
    print(kthLargest.add(5))
    print(kthLargest.add(6))
    print(kthLargest.add(7))
    print(kthLargest.add(8))

