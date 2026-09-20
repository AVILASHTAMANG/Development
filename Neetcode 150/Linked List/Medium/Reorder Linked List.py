# You are given the head of a singly linked-list.
#
# The positions of a linked list of length = 7 for example, can intially be represented as:
#
# [0, 1, 2, 3, 4, 5, 6]
#
# Reorder the nodes of the linked list to be in the following order:
#
# [0, 6, 1, 5, 2, 4, 3]
#
# In the general case, label the nodes by their original zero-based positions from 0 to n - 1. After reordering, those original positions appear in this order:
#
# [0, n-1, 1, n-2, 2, n-3, ...]
#
# These numbers represent node positions, not the values stored in the nodes.
#
# You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # find midpoint of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split the linked list
        second_half = slow.next
        slow.next = None

        # reverse the second list
        curr = second_half
        prev = None
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # merge the 2 list
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        return first.next

if __name__ == '__main__':
    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(6)
    node4 = ListNode(8)
    node5 = ListNode(10)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    Solution().reorderList(node1)

    curr = node1
    res = []
    while curr:
        res.append(str(curr.val))
        curr = curr.next
    print(res)
