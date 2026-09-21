# You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.
#
# Create a deep copy of the list.
#
# The deep copy should consist of exactly n new nodes, each including:
#
# The original value val of the copied node
# A next pointer to the new node corresponding to the next pointer of the original node
# A random pointer to the new node corresponding to the random pointer of the original node
# Note: None of the pointers in the new list should point to nodes in the original list.
#
# Return the head of the copied linked list.
#
# In the examples, the linked list is represented as a list of n nodes. Each node is represented as a pair of [val, random_index] where random_index is the index of the node (0-indexed) that the random pointer points to, or null if it does not point to any node.

from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Using hash map
        if not head:
            return None

        # Pass 1 : Store all the nodes value without pointers
        old_to_new = {}
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # Pass 2 : Assign the next and random pointers
        curr = head
        while curr:
            if curr.next:
                old_to_new[curr].next = old_to_new[curr.next]
            if curr.random:
                old_to_new[curr].random = old_to_new[curr.random]
            curr = curr.next
        return old_to_new[head]

if __name__ == '__main__':
    # 1. Create each node manually for: [[3,null],[7,3],[4,0],[5,1]]
    node0 = Node(3)  # Index 0
    node1 = Node(7)  # Index 1
    node2 = Node(4)  # Index 2
    node3 = Node(5)  # Index 3

    # 2. Connect the 'next' pointers (Sequential chain)
    node0.next = node1
    node1.next = node2
    node2.next = node3

    # 3. Connect the 'random' pointers based on the given indices
    node0.random = None    # [3, null] -> random is None
    node1.random = node3   # [7, 3]    -> random points to index 3 (node3)
    node2.random = node0   # [4, 0]    -> random points to index 0 (node0)
    node3.random = node1   # [5, 1]    -> random points to index 1 (node1)

    head = node0

    # 4. Execute the solution
    solution = Solution()
    copied_head = solution.copyRandomList(head)

    # 5. Print the copied list nodes and their random connections to verify
    curr = copied_head
    print("Verification of Copied List:")
    while curr:
        rand_val = curr.random.val if curr.random else "None"
        print(f"Node Value: {curr.val} | Random Pointer Points To: {rand_val}")
        curr = curr.next

    print("\nAre original and copy distinct objects in memory?", head is not copied_head)