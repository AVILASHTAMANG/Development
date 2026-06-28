# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
# Return the integer that represents the evaluation of the expression.
# The operands may be integers or the results of other operations.
# The operators include '+', '-', '*', and '/'.
# Assume that division between integers always truncates toward zero.

from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {'*','-','+','/'}:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a+b)
                elif token == '-':
                    stack.append(a-b)
                elif token == '*':
                    stack.append(a*b)
                elif token == '/':
                    stack.append(int(a/b))
            else:
                 stack.append(int(token))
        return stack[-1]

if __name__ == '__main__':
    tokens = ["1","2","+","3","*","4","-"]
    print(Solution().evalRPN(tokens))
