# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with
# itself one or more times).
#
# You are given two strings str1 and str2, return the largest string x such that x divides both str1 and str2. If there
# is no such string, return "".

from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        return str1[:gcd(len(str1),len(str2))]
        # def gcd(a,b):
        #     while b:
        #         a,b=b,a%b
        #     return a
        # res = gcd(len(str1), len(str2))
        # return str1[:res]


if __name__=='__main__':
    str1 = "ABAB"
    str2 = "AB"
    print(Solution().gcdOfStrings(str1,str2))