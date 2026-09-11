# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        # s_f = {}
        # t_f = {}

        # for i in range(len(s)):
        #     s_f[s[i]] = s_f.get(s[i], 0) + 1
        #     t_f[t[i]] = t_f.get(t[i], 0) + 1

        # return s_f == t_f

        # for i in range(len(s)):
        #     if s[i] in s_f:
        #         s_f[s[i]] += 1
        #     else:
        #         s_f[s[i]] = 1

        #     if t[i] in t_f:
        #         t_f[t[i]] += 1
        #     else:
        #         t_f[t[i]] = 1

        # return s_f == t_f

        #Most efficient solution if only small case eltters are present
        count =[0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        for num in count:
            if num!=0:
                return False
        return True
