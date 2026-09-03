# Pow(x, n) is a mathematical function to calculate the value of x raised to the power of n (i.e., x^n).
# Given a floating-point value x and an integer value n, implement the myPow(x, n) function, which calculates x raised to the power n.
# You may not use any built-in library functions.
#You should aim for a solution as good or better than O(logn) time and O(logn) space, where n is the given integer.

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x=1/x
            n = -n
        res = 1.0
        while n>0:
            if n%2==1:
                res *= x
            x*=x
            n//=2
        return res

if __name__ == '__main__':
    x= 2.00000
    n = 5
    print(Solution().myPow(x,n))
