# You are given a 2D integer array matrix, return the transpose of matrix.
#
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # return list(zip(*matrix))
        # simple unpacks zip(*matrix) → zip([1,2,3], [4,5,6])
        #             → (1,4), (2,5), (3,6)

        # in-place square matrix only
        # n = len(matrix)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # return matrix

        # below optimized
        rows = len(matrix)
        cols = len(matrix[0])
        res=[[0]*rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
              res[j][i]=matrix[i][j]
        return res

if __name__=='__main__':
    matrix=[[1,0,5],[2,4,3]]
    print(Solution().transpose(matrix))