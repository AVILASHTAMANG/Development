# You are given two strings num1 and num2 that represent non-negative integers.
# Return the product of num1 and num2 in the form of a string.
# Assume that neither num1 nor num2 contain any leading zero, unless they are the number 0 itself.
# Note: You can not use any built-in library to convert the inputs directly into integers.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        res = [0] * (m+n)

        for i in range(m-1,-1,-1):
            digit1 = ord(num1[i]) - ord("0")
            for j in range(n-1,-1,-1):
                digit2 = ord(num2[j]) - ord("0")
                total = digit1 * digit2 + res[i+j+1]
                # remainder
                res[i+j+1] = total % 10
                #carry
                res[i+j] += total//10
        #skip leading zeros
        start_idx = 0
        while start_idx < len(res) and res[start_idx] == 0:
            start_idx += 1
        return "".join(str(d) for d in res[start_idx:])

if __name__ == '__main__':
    a = "111"
    b= "222"
    print(Solution().multiply(a,b))
