# Given an m x n matrix of integers matrix, return a list of all elements within the matrix in spiral order.

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        res = []

        while left <= right and top <= bottom:

            # Move left to right
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            # Move top to bottom
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # Move right to left if row exists
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            # Move bottom to top if column exists
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res

if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(Solution().spiralOrder(matrix))
