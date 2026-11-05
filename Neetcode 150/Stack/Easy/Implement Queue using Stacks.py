# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the
# functions of a normal queue (push, peek, pop, and empty).
#
# Implement the MyQueue class:
#
# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:
#
# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is
# empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque
# (double-ended queue) as long as you use only a stack's standard operations.

class MyQueue:

    def __init__(self):
        self.stack1=[] # for push
        self.stack2=[] # for pop/peek(FIFO order)

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

arguments = ["MyQueue","push","push","pop","push","peek"]
params = [[],[1],[2],[],[3],[]]

if __name__=='__main__':
    obj=MyQueue()
    result = [None]
    for args,param in zip(arguments[1:],params[1:]):
        if args == 'push':
            result.append(obj.push(param))
        elif args=='pop':
            result.append(obj.pop())
        elif args=='peek':
            result.append(obj.peek())
        elif args=='empty':
            result.append(obj.empty())
    print(result)

