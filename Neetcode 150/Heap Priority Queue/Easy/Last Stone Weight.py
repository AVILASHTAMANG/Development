# You are given an array of integers stones where stones[i] represents the weight of the ith stone.
#
# We want to run a simulation on the stones as follows:
#
# At each step we choose the two heaviest stones, with weight x and y and smash them togethers
# If x == y, both stones are destroyed
# If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# Continue the simulation until there is no more than one stone remaining.
#
# Return the weight of the last remaining stone or return 0 if none remain.

### need to use MAX Heap #######
# In Python, the heapq module is strictly designed for min-heaps.
# If you ever need a max-heap using Python('s built-in heapq module, the standard workaround is to multiply all the numbers'
# ' by -1 when you push them in, and multiply them by -1 again when you take them out. This tricks the min-heap into '
# 'behaving like a max-heap!)

# import sys
import heapq
from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        max_heap = heapq.heapify_max(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)
            if stone1 != stone2:
                diff = stone1 - stone2
                heapq.heappush_max(stones, diff)

        return stones[0] if stones else 0

if __name__ =='__main__':
    stones = [3,7,2]
    print(Solution().lastStoneWeight(stones))

