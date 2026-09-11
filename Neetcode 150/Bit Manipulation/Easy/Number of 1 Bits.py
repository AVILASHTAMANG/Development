# You are given an unsigned integer n. Return the number of 1 bits in its binary representation.
# You may assume n is a non-negative integer which fits within 32-bits.

class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        count = 0
        for i in range(32):
            mask = 1 << i
            if (n & mask)!=0:
                count+=1
        return count

if __name__=='__main__':
    n = 2147483645
    print(Solution().hammingWeight(n))
