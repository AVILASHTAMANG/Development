# You are given two strings ransomNote and magazine, return true if ransomNote can be
# constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        f_r = Counter(ransomNote)
        f_m = Counter(magazine)
        for ch in ransomNote:
            if f_m[ch] < f_r[ch]:
                return False
        return True
    #return not (Counter(ransomNote) - Counter(magazine))

if __name__ == '__main__':
    ransomNote = "aa"
    magazine = "aab"
    print(Solution().canConstruct(ransomNote, magazine))