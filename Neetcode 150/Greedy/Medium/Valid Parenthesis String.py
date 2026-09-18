# You are given a string s which contains only three types of characters: '(', ')' and '*'.
#
# Return true if s is valid, otherwise return false.
#
# A string is valid if it follows all of the following rules:
#
# Every left parenthesis '(' must have a corresponding right parenthesis ')'.
# Every right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# A '*' could be treated as a right parenthesis ')' character or a left parenthesis '(' character, or as an empty string "".

class Solution:
    def checkValidString(self, s: str) -> bool:
        # using greedy approach O(n) time and O(1) space
        lo, hi = 0, 0 # minimum and and maximum number open brackets
        for c in s:
            if c == '(':
                lo += 1
                hi += 1
            elif c == ')':
                lo -= 1
                hi -= 1
            else:
                lo -= 1
                hi += 1
            if hi<0:
                return False
            lo = max(lo, 0)
        return lo == 0

        # Using 2 stacks for open brackets and star
        paren, star = [], []
        for i,c in enumerate(s):
            if c == '(':
                paren.append(i)
            elif c == '*':
                star.append(i)
            else:
                if paren:
                    paren.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while paren and star:
            if paren.pop()>star.pop():
                return False
        return not paren


if __name__ == '__main__':
    s = "((**)"
    print(Solution().checkValidString(s))


