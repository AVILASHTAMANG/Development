# You are given a 2D integer array matrix, return the transpose of matrix.
#
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

if __name__=='__main__':
    matrix = [[2, 1],[-1, 3]]
    print(Solution().transpose(matrix))