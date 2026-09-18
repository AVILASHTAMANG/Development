# You are given a string s consisting of lowercase english letters.
#
# We want to split the string into as many substrings as possible, while ensuring that each letter appears in at most one substring.
#
# Return a list of integers representing the size of these substrings in the order they appear in the string.

from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {c:i for i, c in enumerate(s)}
        start, end = 0, 0
        res =[]
        for i, c in enumerate(s):
            end = max(end, last_index[c])
            if i == end:
                res.append(i-start+1)
                start = i+1
        return res

if __name__ == '__main__':
    s = "xyxxyzbzbbisl"
    print(Solution().partitionLabels(s))
