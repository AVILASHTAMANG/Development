# You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from
# A to Z. You are also given an integer n.
#
# Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.
#
# The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.
#
# Return the minimum number of CPU cycles required to complete all tasks.

import heapq
from typing import List
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)
        cooldown_queue = deque() # Stores the remaining count of a particular task and time of availability for execution
        cycle = 0 # CPU cycles

        while max_heap or cooldown_queue:
            cycle += 1

            if max_heap:
                count = -heapq.heappop(max_heap)
                count -= 1
                if count > 0:
                    cooldown_queue.append([count, cycle+n])

            if cooldown_queue and cooldown_queue[0][1] == cycle:
                heapq.heappush(max_heap, -cooldown_queue.popleft()[0])
        return cycle

if __name__ == '__main__':
    tasks = ["X","X","Y","Y"]
    n = 2
    print(Solution().leastInterval(tasks, n))