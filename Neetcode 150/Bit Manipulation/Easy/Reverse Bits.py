# Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result.

class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        for i in range(32):
            bit = (n>>i)&1
            if bit == 1:
                res |= (1<<(31-i))
        return res

if __name__=='__main__':
    n = 0b00000000000000000000000000010101
    print(Solution().reverseBits(n))