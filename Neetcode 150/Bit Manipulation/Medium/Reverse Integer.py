# You are given a signed 32-bit integer x.
# Return x after reversing each of its digits. After reversing, if x goes outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0 instead.
# Solve the problem without using integers that are outside the signed 32-bit integer range.

class Solution:
    def reverse(self, x: int) -> int:
        res, maxint, minint = 0, 2**31-1 , -2**31
        max_div_10 = maxint // 10
        min_div_10 = int(minint / 10)
        while x != 0:
            rem = x % 10 if x > 0 else x % -10
            x = int(x / 10)
            # Positive overflow check
            if res > max_div_10 or (res == max_div_10 and rem > 7):
                return 0
            # Negative underflow check
            if res < min_div_10 or (res == min_div_10 and rem < -8):
                return 0
            res = res * 10 + rem
        return res

if __name__=='__main__':
    #x = -1234
    x = -1563847412
    #x = 1234236467
    print(Solution().reverse(x))