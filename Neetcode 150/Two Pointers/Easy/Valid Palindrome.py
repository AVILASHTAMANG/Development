#Given a string s, return true if it is a palindrome, otherwise return false.
#A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
#Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).
#You should aim for a solution with O(n) time and O(1) space, where n is the length of the input string.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        while (start<end):
            while start<end and not s[start].isalnum():
                start += 1
            while start<end and not s[end].isalnum():
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True

if __name__ == '__main__':
    s = "Was it a car or a cat I saw?"
    obj = Solution()
    print(obj.isPalindrome(s))
