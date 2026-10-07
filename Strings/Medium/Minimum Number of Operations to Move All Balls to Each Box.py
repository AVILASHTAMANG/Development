# You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the i-th box is empty,
# and '1' if it contains one ball.
# In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1.
# Note that after doing so, there may be more than one ball in some boxes.
# Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to
# the i-th box.
# Each answer[i] is calculated considering the initial state of the boxes.

from typing import List
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # Brute force (O(n2))
        # ans = []
        # for i in range(len(boxes)):
        #     first = 0
        #     second = 0
        #     for k in range(i):
        #         count = 0
        #         if boxes[k] != '0':
        #             count = abs(k-i)
        #         first += count
        #     for j in range(i+1, len(boxes)):
        #         count1 = 0
        #         if boxes[j] != '0':
        #             count1 = abs(j-i)
        #         second += count1
        #     ans.append(abs(second+first))
        # return ans

        # Optimize Two-pass approach
        n = len(boxes)
        ans = [0] * n

        # left to right pass
        balls = 0
        operations = 0
        for i in range(n):
            ans[i] += operations
            balls += int(boxes[i])
            operations += balls

        # right to left pass
        balls = 0
        operations = 0
        for i in range(n-1, -1, -1):
            ans[i] += operations
            balls += int(boxes[i])
            operations += balls

        return ans



if __name__ == '__main__':
    boxes = "001011"
    print(Solution().minOperations(boxes))