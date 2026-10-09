# You are given a string s which represents an expression, evaluate this expression and return its value.
#
# The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid. All intermediate results will be in the range of
# [-(2^31), (2^31)-1].
#
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions,
# such as eval().

class Solution:
    def calculate(self, s: str) -> int:
        curr_num = 0
        stack = []
        last_operator = '+'
        for i, char in enumerate(s):
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            if char in "+-*/" or i == len(s)-1:
                if last_operator == '+':
                    stack.append(curr_num)
                elif last_operator == '-':
                    stack.append(-curr_num)
                elif last_operator == '*':
                    stack.append(int(stack.pop() * curr_num))
                elif last_operator == '/':
                    stack.append(int(stack.pop() / curr_num))
                last_operator = char
                curr_num = 0
        return sum(stack)

if __name__ == '__main__':
    s = " 3+5 / 2 "
    print(Solution().calculate(s))