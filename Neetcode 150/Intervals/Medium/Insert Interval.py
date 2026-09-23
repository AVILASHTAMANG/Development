# You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] represents the start and the end time of the ith interval. intervals is initially sorted in ascending order by start_i.
#
# You are given another interval newInterval = [start, end].
#
# Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and also intervals still does not have any overlapping intervals. You may merge the overlapping intervals if needed.
#
# Return intervals after adding newInterval.
#
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])

            elif intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                newInterval = intervals[i]

            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        res.append(newInterval)
        return res

if __name__ == '__main__':
    intervals = [[1, 3], [4, 6]]
    newInterval = [2,5]
    print(Solution().insert(intervals, newInterval))
