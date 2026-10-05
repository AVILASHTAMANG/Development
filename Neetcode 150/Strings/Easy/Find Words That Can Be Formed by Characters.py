# You are given an array of strings words and a string chars.
#
# A string is good if it can be formed by characters from chars (each character can only be used once for
# each word in words).
#
# Return the sum of lengths of all good strings in words.

from typing import List
from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        f_chars = Counter(chars)
        res = 0
        for ch in words:
            f_words = Counter(ch)
            count = 0
            for i in range(len(ch)):
                if f_words[ch[i]] <= f_chars[ch[i]]:
                    count += 1
            if count == len(ch):
                res += len(ch)

            # if all(f_words[c] <= f_chars[c] for c in f_words):
            #     res += len(ch)

            # for ch in words:
            #     if not (Counter(ch) - f_chars):
            #         res += len(ch)
        return res



if __name__ == '__main__':
    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"
    print(Solution().countCharacters(words, chars))