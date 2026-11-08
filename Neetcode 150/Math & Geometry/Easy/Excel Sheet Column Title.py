# You are given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res=[]
        while columnNumber>0:
            columnNumber-=1 # whenever column number is multiple of 26 remainder is 0 and should be mapped to 'Z' instead of "A
            res.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26
        return ''.join(reversed(res))

if __name__=='__main__':
    columnNumber = 32
    print(Solution().convertToTitle(columnNumber))