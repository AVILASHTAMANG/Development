#You are given two strings s1 and s2.
#Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.
#Both strings only contain lowercase letters.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n>m:
            return False
        count1 = [0] * 26
        count2 = [0] * 26
        for i in range(n):
            # count frequencies in s1
            count1[ord(s1[i]) - ord('a')] += 1
            # initialize first window in s2
            count2[ord(s2[i]) - ord('a')] += 1
        if count1 == count2:
            return True
        for i in range(n,m):
            # slide the window accordingly
            # add new element to window
            count2[ord(s2[i]) - ord('a')] += 1
            #remove old element from window
            count2[ord(s2[i-n]) - ord('a')] -= 1
            if count1 == count2:
                return True
        return False

if __name__ == '__main__':
    s1 = "abc"
    s2 = "lecabee"
    print(Solution().checkInclusion(s1,s2))
