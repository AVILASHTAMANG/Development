# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
#
# The new list should be made up of nodes from list1 and list2.

from typing import Optional
#Definition of a Singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2 # if any node is remaining
        return dummy.next

if __name__ == '__main__':
    list1 = ListNode(1, ListNode(2,ListNode(4)))
    list2 = ListNode(1,ListNode(3,ListNode(5)))
    merged = Solution().mergeTwoLists(list1, list2)
    res = []
    while merged:
        res.append(merged.val)
        merged = merged.next
    print(res)