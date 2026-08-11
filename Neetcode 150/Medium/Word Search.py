#Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.
#For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        def dfs(i,j,s):
            if i <0 or i==m or j<0 or j==n:
                return False
            if board[i][j] != word[s] or board[i][j]=="#":
                return False
            if s == len(word)-1:
                return True
            temp = board[i][j]
            board[i][j]="#"
            isexist = dfs(i+1,j,s+1) or dfs(i-1,j,s+1) or dfs(i,j-1,s+1) or dfs(i,j+1,s+1)
            board[i][j]=temp
            return isexist
        return any(dfs(i,j,0) for i in range(m) for j in range(n))

if __name__ == '__main__':
    board = [
        ["A", "B", "C", "D"],
        ["S", "A", "A", "T"],
        ["A", "C", "A", "E"]
    ]
    word = "CAT"
    print(Solution().exist(board,word))
