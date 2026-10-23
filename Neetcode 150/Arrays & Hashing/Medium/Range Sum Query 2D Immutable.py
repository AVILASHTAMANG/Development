'''
# You are given a 2D matrix matrix, handle multiple queries of the following type:
#
# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1)
# and lower right corner (row2, col2).
# Implement the NumMatrix class:
#
# NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the
# rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# You must design an algorithm where sumRegion works on O(1) time complexity.

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        m, n = len(matrix), len(matrix[0])
        # Precomputing the Prefix Matrix : pref matrix has dimensions (m + 1) x (n + 1) initialized to 0
        
        # 1. Precomputing the Prefix Matrix
        # For every cell (r, c)  in the (m+1) \times (n+1) prefix array:
        # {pref}[r][c] = {pref}[r - 1][c] + {pref}[r][c - 1] - {pref}[r - 1][c - 1] + {matrix}[r - 1][c - 1]
        # {pref}[r - 1][c]: Sum of the rectangle above.
        # {pref}[r][c - 1]: Sum of the rectangle to the left.
        # -{pref}[r - 1][c - 1]: Subtract the overlapping top-left region because it was added twice.
        # +{matrix}[r - 1][c - 1]: Add the current cell value.
        self.pref = [[0] * (n+1) for _ in range(m+1)]

        for r in range(m):
            for c in range(n):
                self.pref[r+1][c+1] = (
                    self.pref[r][c+1] + self.pref[r+1][c] - self.pref[r][c] + matrix[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Querying sumRegion(row1, col1, row2, col2)
        # To retrieve the sum inside [row1, row2] \times [col1, col2]   in O(1):
        # {Total} = {pref}[row2 + 1][col2 + 1] - {pref}[row1][col2 + 1] - {pref}[row2 + 1][col1] + {pref}[row1][col1]
        # Start with the full rectangle ending at (row2, col2): pref[row2 + 1][col2 + 1].
        # Remove the rectangle strictly above row1: pref[row1][col2 + 1].
        # Remove the rectangle strictly to the left of col1: pref[row2 + 1][col1].
        # 
        # Add back the top-left corner that was subtracted twice: pref[row1][col1].

        return (
                self.pref[row2 + 1][col2 + 1]
                - self.pref[row1][col2 + 1]
                - self.pref[row2 + 1][col1]
                + self.pref[row1][col1]
        )

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# Input: ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
# [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2],
#  [1, 2, 2, 4]]
#
# Output: [null, 8, 11, 12]
'''

from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return

        m, n = len(matrix), len(matrix[0])
        # (m + 1) x (n + 1) prefix grid initialized to 0
        self.pref = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m):
            for c in range(n):
                self.pref[r + 1][c + 1] = (
                        self.pref[r][c + 1]
                        + self.pref[r + 1][c]
                        - self.pref[r][c]
                        + matrix[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
                self.pref[row2 + 1][col2 + 1]
                - self.pref[row1][col2 + 1]
                - self.pref[row2 + 1][col1]
                + self.pref[row1][col1]
        )


# --- Driver code to test the implementation ---
if __name__ == "__main__":
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]

    # 1. Initialize the object
    numMatrix = NumMatrix(matrix)

    # 2. Call sumRegion queries
    print("Query (2, 1, 4, 3):", numMatrix.sumRegion(2, 1, 4, 3))  # Output: 8
    print("Query (1, 1, 2, 2):", numMatrix.sumRegion(1, 1, 2, 2))  # Output: 11
    print("Query (1, 2, 2, 4):", numMatrix.sumRegion(1, 2, 2, 4))  # Output: 12
