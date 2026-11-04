# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the
# functions of a normal stack (push, top, pop, and empty).
#
# Implement the MyStack class:
#
# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:
#
# You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and
# is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque
# (double-ended queue) as long as you use only a queue's standard operations.

from collections import deque
class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        return self.queue1.append(x)

    def pop(self) -> int:
        while len(self.queue1)>1:
            self.queue2.append(self.queue1.popleft())
        top = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top

    def top(self) -> int:
        while len(self.queue1)>1:
            self.queue2.append(self.queue1.popleft())
        t = self.queue1[0]
        self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1
        return t

    def empty(self) -> bool:
        return len(self.queue1) == 0

# Your MyStack object will be instantiated and called as such:
arguments = ["MyStack", "push", "push", "top", "pop", "empty"]
params = [[], [1], [2], [], [], []]
if __name__ == '__main__':
    obj = MyStack()
    result = [None]  # "MyStack" → null
    for name, params in zip(arguments[1:], params[1:]):
        if name == 'push':
            obj.push(params[0])
            result.append(None)
        elif name == 'pop':
            result.append(obj.pop())
        elif name == 'top':
            result.append(obj.top())
        elif name == 'empty':
            result.append(obj.empty())
    print(result)


# Input: ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
#
# Output: [null, null, null, 2, 2, false]