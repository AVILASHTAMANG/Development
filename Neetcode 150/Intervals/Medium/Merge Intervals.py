# Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.
# You may return the answer in any order.

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []
        for interval in intervals:
            if not res or res[-1][1]<interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res

if __name__ == '__main__':
    intervals=[[1,2],[2,3]]
    print(Solution().merge(intervals))