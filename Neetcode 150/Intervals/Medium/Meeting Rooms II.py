# Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of rooms required to schedule all meetings without
# any conflicts.

from typing import List
# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # start = [intervals[i][0] for i in range(len(intervals))]
        # end = [intervals[i][1] for i in range(len(intervals))]

        # start = [i[0] for i in intervals]
        # end = [i[1] for i in intervals]

        start = [i.start for i in intervals]
        end = [i.end for i in intervals]

        start.sort()
        end.sort()

        curr_rooms = 0
        max_rooms = 0
        s = 0
        e = 0
        while s<len(intervals):
            if start[s] < end[e]:
                curr_rooms += 1
                max_rooms = max(curr_rooms, max_rooms)
                s += 1
            else:
                e += 1
                curr_rooms -= 1
                max_rooms = max(curr_rooms, max_rooms)

        return max_rooms

if __name__ == '__main__':
    # intervals = [(0,40),(5,10),(15,20)]
    # Create actual Interval objects for local testing
    intervals = [Interval(0, 40), Interval(5, 10), Interval(15, 20)]
    print(Solution().minMeetingRooms(intervals))





