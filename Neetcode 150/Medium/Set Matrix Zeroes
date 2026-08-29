#Given an m x n matrix of integers matrix, if an element is 0, set its entire row and column to 0's.
#You must update the matrix in-place.
#Follow up: Could you solve it using O(1) space?

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row_zero = False
        first_col_zero = False
        rows, cols = len(matrix), len(matrix[0])

        #Determine if first row or first col has any zero
        for c in range(0,cols):
            if matrix[0][c] == 0:
                first_row_zero = True
                break
        
        for r in range(0,rows):
            if matrix[r][0]==0:
                first_col_zero = True
                break

        #Using first_row_zero and first_col_zero as markers        
        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[r][c]==0:
                    matrix[0][c]=0
                    matrix[r][0]=0

        #zero out inner cells based on markers
        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[r][0]==0 or matrix[0][c]==0:
                    matrix[r][c]=0

        # Zero out the first column if needed
        if first_col_zero:
            for r in range(rows):
                matrix[r][0]=0
        
        # Zero out the first row if needed
        if first_row_zero:
            for c in range(cols):
                matrix[0][c]=0
