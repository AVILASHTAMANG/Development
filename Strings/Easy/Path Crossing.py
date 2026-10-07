# You are given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving
# one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane
# and walk on the path specified by path.
#
# Return true if the path crosses itself at any point, that is, if at any time you are on a location
# you have previously visited. Return false otherwise.

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        x, y = 0, 0
        visited.add((x, y))
        for ch in path:
            if ch == 'N':
                y += 1
            elif ch == 'E':
                x -= 1
            elif ch == 'W':
                x += 1
            else:
                y -= 1
            if (x,y) in visited:
                return True
            else:
                visited.add((x, y))
        return False


if __name__=='__main__':
    path = "NESWW"
    print(Solution().isPathCrossing(path))