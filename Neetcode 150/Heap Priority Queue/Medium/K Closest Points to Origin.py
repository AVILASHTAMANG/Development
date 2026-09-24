# You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y
# axis plane. You are also given an integer k.
# Return the k closest points to the origin (0, 0).
# The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).
# You may return the answer in any order. The answer is guaranteed to be unique(except for the order in which the
# points are returned.)

from typing import List
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x,y in points:
            distance = (x**2 + y**2) ** 0.5
            heapq.heappush(min_heap, (distance, [x, y]))
        res = []
        for _ in range(k):
            distance, point = heapq.heappop(min_heap)
            res.append(point)
        return res

if __name__ == '__main__':
    points = [[0, 2], [2, 0], [2, 2]]
    k = 2
    print(Solution().kClosest(points, k))