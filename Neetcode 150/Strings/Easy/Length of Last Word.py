# You are given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        return len(s.split()[-1])


if __name__=='__main__':
    s = "   fly me   to   the moon  "
    print(Solution().lengthOfLastWord(s))