# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

from typing import Optional
#Definition of a Singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next # temporarily store the next node
            curr.next = prev # reverse the pointer backward
            prev = curr # shift prev forward
            curr = next_temp # shift curr forward
        return prev # prev becomes the new head of the reversed list

if __name__ == '__main__':
    # 1. Create a Linked list: 0 -> 1 ->2 -> 3 -> None
    head = ListNode(0,ListNode(1, ListNode(2, ListNode(3))))

    # 2. Reverse the linked list
    reversed_head = Solution().reverseList(head)

    # 3. Print the reversed linked list by traversing it
    curr = reversed_head
    res = []
    while curr:
        res.append(curr.val)
        curr = curr.next

    print(res)

