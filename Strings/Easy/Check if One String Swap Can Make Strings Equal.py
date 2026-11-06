# The strings s1 and s2 have equal length. You may swap two character positions in exactly one of the strings, at most
# once. The chosen positions may be the same, and you may also perform no swap. Return true if the strings can become
# equal, or false otherwise.

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        mismatches={}
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                mismatches[i]=(s1[i],s2[i])
        if len(mismatches)==0:
            return True
        if len(mismatches) == 2:
            i, j =mismatches.keys()
            return mismatches[i][0]==mismatches[j][1] and mismatches[j][0]==mismatches[i][1]
        return False
        pass

if __name__=='__main__':
    s1 = "abcd"
    s2 = "abdc"
    print(Solution().areAlmostEqual(s1,s2))