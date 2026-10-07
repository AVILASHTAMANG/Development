# You are given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1

if __name__ == '__main__':
    # haystack = "neetcodeneetcode"
    # needle = "neet"
    haystack = "neetcode"
    needle = "codem"
    print(Solution().strStr(haystack, needle))
