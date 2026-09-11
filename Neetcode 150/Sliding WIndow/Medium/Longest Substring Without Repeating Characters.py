# Given a string s, find the length of the longest substring without duplicate characters.
# A substring is a contiguous sequence of characters within a string.

from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        max_len = 0
        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            max_len=max(max_len, right-left+1)
        return max_len

if __name__=='__main__':
    s = "zxyzxyz"
    print(Solution().lengthOfLongestSubstring(s))