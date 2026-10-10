# You are given a string s, return the length of the longest substring between two equal characters, excluding
# the two characters. If there is no such substring return -1.
#
# A substring is a contiguous sequence of characters within a string.

from collections import Counter
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        found = {}
        max_length = -1
        for i, ch in enumerate(s):
            if ch in found:
                max_length = max(max_length, i-found[ch]-1)
            else:
                found[ch] = i
        return max_length

if __name__ == '__main__':
    s = "abca"
    print(Solution().maxLengthBetweenEqualCharacters(s))