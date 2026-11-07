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
        self.queue = [0] * k # A fixed-length list self.queue of size k holds the values without dynamic resizing.
        # Maintaining self.head and self.count simplifies distinguishing between full and empty states without needing
        # dummy slots or complex pointer checks:
        # ◦ Empty: count == 0
        # ◦ Full: count == capacity
        self.capacity=k
        self.head=0
        self.count=0

    # Circular Wrapping:
    # ◦ Insertion index: (head + count) % capacity
    # ◦ Rear access index: (head + count - 1) % capacity
    # ◦ Deletion index update: (head + 1) % capacity
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        # Calculate insertion index using circular indexing
        tail = (self.head+self.count)%self.capacity
        self.queue[tail] = value
        self.count+=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        # move ahead forward circularly and decrement size count
        self.head=(self.head+1)%self.capacity
        self.count-=1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        #the rear is at below index
        tail=(self.head+self.count-1)%self.capacity
        return self.queue[tail]

    def isEmpty(self) -> bool:
        return self.count==0

    def isFull(self) -> bool:
        return self.count==self.capacity

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

if __name__=='__main__':
    obj = None
    results = []

    for op, param in zip(operations, params):
        if op == "MyCircularQueue":
            obj = MyCircularQueue(param[0])
            results.append(None)
        elif op == "enQueue":
            results.append(obj.enQueue(param[0]))
        elif op == "deQueue":
            results.append(obj.deQueue())
        elif op == "Front":
            results.append(obj.Front())
        elif op == "Rear":
            results.append(obj.Rear())
        elif op == "isEmpty":
            results.append(obj.isEmpty())
        elif op == "isFull":
            results.append(obj.isFull())

    print(results)