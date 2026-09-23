# Given an array of intervals intervals where intervals[i] = [start_i, end_i], return the minimum number of
# intervals you need to remove to make the rest of the intervals non-overlapping.

from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        prevEnd = intervals[0][1]
        count = 0
        i = 1
        while i < len(intervals):
            if intervals[i][0] >= prevEnd:
                prevEnd = intervals[i][1]
            else:
                count += 1
            i += 1
        return count

if __name__ == '__main__':
    intervals = [[1,2],[2,4],[1,4]]
    print(Solution().eraseOverlapIntervals(intervals))