# Given a string s, split s into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.
# You may return the solution in any order.

from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def ispalindrome(left,right):
            while left<right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        def backtrack(start,path):
            if start == len(s):
                res.append(path[:])
            for end in range(start, len(s)):
                if ispalindrome(start,end):
                    path.append(s[start:end+1])
                    backtrack(end+1,path)
                    path.pop()
        backtrack(0,[])
        return res

if __name__ == '__main__':
    s = "aab"
    print(Solution().partition(s))
