# Given two integers a and b, return the sum of the two integers without using the + and - operators.

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF # 32 bits containing all 1s. This is used to keep only the lowest 32 bits. It's used because Python integers don't naturally behave like 32-bit integers.
        max_int = 0x7FFFFFFF # This is the largest signed 32-bit integer.
        while b!=0:
            carry = (a&b)<<1
            a = (a^b)&mask
            b = carry & mask
        return a if a<=max_int else a-(mask+1)

if __name__=='__main__':
    a = -12
    b = -8
    print(Solution().getSum(a,b))