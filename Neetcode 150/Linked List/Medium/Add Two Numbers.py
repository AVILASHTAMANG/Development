# You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.
#
# The digits are stored in reverse order, e.g. the number 321 is represented as 1 -> 2 -> 3 -> in the linked list.
#
# Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Return the sum of the two numbers as a linked list.

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0
        while l1 is not None or l2 is not None or carry>0:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            s = val1 + val2+ carry
            carry = s // 10
            curr_node = s % 10
            tail.next = ListNode(curr_node)
            tail = tail.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return dummy.next

if __name__ == '__main__':
    list1 = ListNode(1, ListNode(2,ListNode(3)))
    list2 = ListNode(4,ListNode(5,ListNode(6)))
    res = Solution().addTwoNumbers(list1, list2)
    while res:
        print(res.val, end='')
        res = res.next

