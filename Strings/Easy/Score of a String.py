# You are given a string s. The score of a string is defined as the sum of the absolute difference between the
# ASCII values of adjacent characters.
# Return the score of s.


class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(s[i]) - ord(s[i-1])) for i in range(1, len(s)))
        # prev = s[0]
        # score = 0
        # for i in range(1, len(s)):
        #     score += abs(ord(s[i]) - ord(prev))
        #     prev = s[i]
        # return score

if __name__ == '__main__':
    s = "neetcode"
    print(Solution().scoreOfString(s))