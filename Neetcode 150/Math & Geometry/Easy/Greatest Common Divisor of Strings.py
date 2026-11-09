# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with
# itself one or more times).
#
# You are given two strings str1 and str2, return the largest string x such that x divides both str1 and str2. If there
# is no such string, return "".

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

if __name__=='__main__':
    str1 = "ABAB"
    str2 = "AB"
    print(Solution().gcdOfStrings(str1,str2))