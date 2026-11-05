# You are given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes
# of the list from position left to position right (1-indexed), and return the reversed list.
from multiprocessing import dummy


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        pre = dummy

        # 1. Reach the node right before index 'left'
        for _ in range(left - 1):
            pre = pre.next

        # 'curr' is the first node of the segment to be reversed
        curr = pre.next

        # 2. Repeatedly shift 'nxt' to immediately after 'pre'
        for _ in range(right - left):
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = pre.next
            pre.next = nxt

        return dummy.next


if __name__=='__main__':
    #head = [1, 2, 3, 4, 5] # Output: [3,2,1,4,5]
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    curr = Solution().reverseBetween(head, left=1, right=3)
    while curr:
        print(curr.val, end=' -> ' if curr.next else '\n')
        curr = curr.next