# You are given a string s of zeros and ones, return the maximum score after splitting the string into two
# non-empty substrings (i.e. left substring and right substring).
#
# The score after splitting a string is the number of zeros in the left substring plus the number of ones
# in the right substring.

class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        left_zeros = 0
        right_ones = s.count('1')
        for i in range(len(s)-1):
            if s[i] == '0':
                left_zeros += 1
            else:
                right_ones -= 1
            max_score = max(max_score, left_zeros + right_ones)
        return max_score

if __name__=='__main__':
    s = "011101"
    print(Solution().maxScore(s))