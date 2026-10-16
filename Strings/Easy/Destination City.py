# Each pair in paths describes a directed trip from its first city to its second city. Together, the paths
# form one continuous route without a cycle, although the pairs can appear in any order. Return the final city
# on the route: it has no outgoing trip. City names are case-sensitive and may contain spaces.

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts = set()
        for path in paths:
            starts.add(path[0])
        for path in paths:
            if path[1] not in starts:
                return path[1]

if __name__ == '__main__':
    paths = [["Cedar", "Oak"], ["Maple", "Cedar"]] # OP : "Oak"
    print(Solution().destCity(paths))