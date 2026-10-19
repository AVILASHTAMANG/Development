# You are given a string s, return true if the s can be a palindrome after deleting at most one character from it.
#
# A palindrome is a string that reads the same forward and backward.
#
# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

from collections import Counter
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left, right):
            while left<right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        left = 0
        right = len(s)-1
        while left<right:
            if s[left] != s[right]:
                return (is_palindrome(left+1, right) or is_palindrome(left, right - 1))
                left += 1
                right -= 1
        return True

if __name__=='__main__':
    s = "abbadc"
    #s = "aca"
    print(Solution().validPalindrome(s))