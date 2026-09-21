#Given the head of a linked list and an integer n, remove the nth node from the end of the list and return its head.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = dummy
        second = dummy
        for _ in range(n+1):
            first = first.next
        while(first):
            second = second.next
            first = first.next
        second.next = second.next.next
        return dummy.next

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    Solution().removeNthFromEnd(node1, 1)

    curr = node1
    res = []
    while curr:
        res.append(str(curr.val))
        curr = curr.next
    print(res)