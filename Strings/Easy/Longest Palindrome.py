# You are given a string s which consists of lowercase or uppercase letters, return the
# length of the longest palindrome that can be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        freq = Counter(s)
        odd_flag = 0
        for val in freq.values():
            if val%2 == 0:
                length += val
            else:
                length += val-1
                odd_flag = 1
        length = (length+1 if odd_flag else length)
        return length


if __name__ == '__main__':
    s = "a"
    print(Solution().longestPalindrome(s)) #dccaccd