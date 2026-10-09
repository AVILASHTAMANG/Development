# You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change
# any '0' to '1' or vice versa.
#
# The string is called alternating if no two adjacent characters are equal. For example, the string
# "010" is alternating, while the string "0100" is not.
#
# Return the minimum number of operations needed to make s alternating.

class Solution:
    def minOperations(self, s: str) -> int:
        count_0, count_1 = 0, 0
        for i in range(len(s)):
            pattern_0 = '0' if i%2==0 else '1'
            pattern_1 = '1' if i%2==0 else'0'
            if s[i] != pattern_0:
                count_0 += 1
            if s[i] != pattern_1:
                count_1 += 1
        return min(count_0, count_1)

if __name__ == '__main__':
    s = "0100"
    print(Solution().minOperations(s))
