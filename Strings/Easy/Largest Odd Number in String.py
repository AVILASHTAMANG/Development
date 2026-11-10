# num contains the decimal digits of a large integer. Among all nonempty contiguous substrings representing odd
# integers, return the one with the greatest numeric value as a string. If none exists, return an empty string.
# The input may be too large for a fixed-width integer.
#
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2!=0:
                return num[:i+1]
        return ""
        pass

if __name__=='__main__':
    num = "2"
    print(Solution().largestOddNumber(num))