# Design and implement circular queue. The circular queue is a linear data structure in which the operations are
# performed based on FIFO (First In First Out) principle, and the last position is connected back to the first
# position to make a circle. It is also called "Ring Buffer".
#
# One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal
# queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue.
# But using the circular queue, we can use the space to store new values.
#
# Implement the MyCircularQueue class:
#
# MyCircularQueue(k) Initializes the object with the size of the queue to be k.
# int Front() Gets the front item from the queue. If the queue is empty, return -1.
# int Rear() Gets the last item from the queue. If the queue is empty, return -1.
# boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
# boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
# boolean isEmpty() Checks whether the circular queue is empty or not.
# boolean isFull() Checks whether the circular queue is full or not.
# You must solve the problem without using the built-in queue data structure in your programming language.

class MyCircularQueue:

    def __init__(self, k: int):

    def enQueue(self, value: int) -> bool:

    def deQueue(self) -> bool:

    def Front(self) -> int:

    def Rear(self) -> int:

    def isEmpty(self) -> bool:

    def isFull(self) -> bool:

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

operations = ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
params = [[3], [1], [2], [3], [4], [], [], [], [4], []]