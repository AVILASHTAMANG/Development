# You are given an array of strings names, and an array heights that consists of distinct positive integers.
# Both arrays are of length n.
#
# For each index i, names[i] and heights[i] denote the name and height of the i-th person.
#
# Return names sorted in descending order by the people's heights.

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = sorted(zip(heights, names), reverse=True)
        return [names for heights, names in people]

if __name__ == '__main__':
    names = ["Mary", "John", "Emma"]
    heights = [180, 165, 170]
    print(Solution().sortPeople(names, heights))
