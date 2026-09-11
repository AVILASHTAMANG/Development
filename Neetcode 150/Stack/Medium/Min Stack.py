# Design a stack class that supports the push, pop, top, and getMin operations.
#
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# Each function should run in O(1) time.

from typing import List
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

if __name__ == "__main__":
    ms = MinStack()
    ms.push(1)
    ms.push(2)
    ms.push(0)
    print(ms.getMin())
    ms.pop()
    print(ms.top())
    print(ms.getMin())

