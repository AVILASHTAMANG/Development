# You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:
# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false
# Note: A board does not need to be full or be solvable to be valid.

from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ####using set#####
        # rows = [set() for _ in range(9)]
        # cols = [set() for _ in range(9)]
        # boxes = [set() for _ in range(9)]
        # for r in range(9):
        #     for c in range(9):
        #         val = board[r][c]
        #         if val == ".":
        #             continue
        #         box = (r//3)*3 + (c//3)
        #         if val in rows[r] or val in cols[c] or val in boxes[box]:
        #             return False
        #         rows[r].add(val)
        #         cols[c].add(val)
        #         boxes[box].add(val)
        # return True
        

        ###using Hashmap#####
        seen = {}
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                row_key = (num,"row",r)
                col_key = (num,"col",c)
                box_key = (num,"box",r//3, c//3)
                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                seen[row_key]=True
                seen[col_key]=True
                seen[box_key]=True
        return True

if __name__ == '__main__':
    board = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
     ["4", ".", ".", "5", ".", ".", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", ".", "3"],
     ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
     [".", ".", ".", "8", ".", "3", ".", ".", "5"],
     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", ".", ".", ".", ".", ".", "2", ".", "."],
     [".", ".", ".", "4", "1", "9", ".", ".", "8"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    obj = Solution()
    print(obj.isValidSudoku(board))