# You are given two binary strings a and b, return their sum as a binary string.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = []
        i=len(a)-1
        j=len(b)-1
        while i>=0 or j>=0:
            a_digit = int(a[i]) if i>=0 else 0
            b_digit = int(b[j]) if j>=0 else 0
            sums = a_digit + b_digit + carry
            res.append(str(sums % 2))
            carry = sums // 2
            j-=1
            i-=1
        if carry:
            res.append(str(carry))
        return ''.join(reversed(res))

if __name__=='__main__':
    a = "101"
    b = "10"
    print(Solution().addBinary(a,b))