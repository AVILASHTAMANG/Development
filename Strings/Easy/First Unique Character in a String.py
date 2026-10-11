# You are given a string s, find the first non-repeating character in it and return its index. If it does not exist,
# return -1.

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        return -1


if __name__ == '__main__':
    s = "neetcodeneet"
    print(Solution().firstUniqChar(s))