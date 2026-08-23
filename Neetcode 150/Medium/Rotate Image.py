# Given a square n x n matrix of integers matrix, rotate it by 90 degrees clockwise.
# You must rotate the matrix in-place. Do not allocate another 2D matrix and do the rotation.

from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        #reverse the rows
        for i in range(n//2):
            matrix[i],matrix[n-i-1] = matrix[n-i-1], matrix[i]
            # transpose of matrix
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

if __name__=='__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(matrix)
    print(matrix)
