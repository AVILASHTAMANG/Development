# You are given an array of strings strs. Return the longest common prefix of all the strings.
#
# If there is no longest common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if i>=len(s) or s[i]!=strs[0][i]:
                    return strs[0][:i]
        return strs[0]

if __name__ == '__main__':
    strs=["flower","flow","flight"]
    print(Solution().longestCommonPrefix(strs))