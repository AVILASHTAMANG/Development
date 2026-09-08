# You are given a stream of points consisting of x-y coordinates on a 2-D plane. Points can be added and queried as follows:
#
# Add - new points can be added to the stream into a data structure. Duplicate points are allowed and should be treated as separate points.
# Query - Given a single query point, count the number of ways to choose three additional points from the data structure such
# that the three points and the query point form a square. The square must have all sides parallel to the x-axis and y-axis,
# i.e. no diagonal squares are allowed. Recall that a square must have four equal sides.
# Implement the CountSquares class:
#
# CountSquares() Initializes the object.
# void add(int[] point) Adds a new point point = [x, y].
# int count(int[] point) Counts the number of ways to form valid squares with point point = [x, y] as described above.

from typing import List
class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        pts = tuple(point)
        if pts in self.points:
            self.points[pts]+=1
        else:
            self.points[pts]=1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        total_squares = 0
        for (x2,y2), count in self.points.items():
            if x1!=x2 or y1==y2:
                continue
            side = abs(y2-y1)
            # Test both directions (right: +side, left: -side)
            for dx in (side, -side):
                p3 = (x1+dx, y1)
                p4 = (x1+dx, y2)
                if p3 in self.points and p4 in self.points:
                    total_squares+= count * self.points[p3] * self.points[p4]
        return total_squares


if __name__ == '__main__':
    commands = [
        "CountSquares",
        "add",
        "add",
        "add",
        "count",
        "count",
        "add",
        "count",
    ]
    arguments = [
        [],
        [[1, 1]],
        [[2, 2]],
        [[1, 2]],
        [[2, 1]],
        [[3, 3]],
        [[2, 2]],
        [[2, 1]],
    ]

    obj = None
    output = []

    for cmd, arg in zip(commands, arguments):
        if cmd == "CountSquares":
            obj = CountSquares()
            output.append(None)
        elif cmd == "add":
            obj.add(arg[0])
            output.append(None)
        elif cmd == "count":
            output.append(obj.count(arg[0]))

    print(output)
