# You are given a string s consisting of lowercase English characters, as well as opening
# and closing parentheses, ( and ).
#
# Your task is to remove the minimum number of parentheses so that the resulting string is valid.
#
# Return the resulting string after removing the invalid parentheses.
#
# A parentheses string is valid if all of the following conditions are met:
#
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open = 0
        ans = []
        res = []
        # left to right pass
        for ch in s:
            if 'a' <= ch and 'z' >= ch:
                ans.append(ch)
            elif ch == "(":
                open += 1
                ans.append(ch)
            elif ch == ")" and open>=1:
                open -= 1
                ans.append(ch)
        # # right to left pass
        for ch in reversed(ans):
            if ch == '(' and open > 0:
                open -= 1
            else:
                res.append(ch)
        return ''.join(reversed(res))

if __name__ == '__main__':
    # s = "nee(t(c)o)de)"
    s = "))()(("
    print(Solution().minRemoveToMakeValid(s))

