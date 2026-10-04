# You are given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and
# a non-empty word in s. Specifically:
#
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.

from collections import Counter
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # s_list = s.split()
        # fs = Counter(s_list)
        # fp = Counter(pattern)
        # if sorted(fp.values()) == sorted(fs.values()):
        #     return True
        # return False

        words = s.split()
        if len(pattern) != len(words):
            return False
        c2w = {}
        w2c = {}
        for c, w in zip(pattern, words):
            if (c in c2w and c2w[c] != w) or (w in w2c and w2c[w] != c):
                return False
            w2c[w] = c
            c2w[c] = w
        return True

if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"
    print(Solution().wordPattern(pattern, s))