# A word is uncommon if it occurs exactly once in one sentence and never in the other. Given the sentences s1 and s2,
# return all uncommon words in any order. Each sentence contains lowercase English words separated by single spaces,
# with no leading or trailing spaces.

from typing import List
from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # words1 = s1.split()
        # words2 = s2.split()
        # freq = {}
        # for word in (words1 + words2):
        #     freq[word] = freq.get(word, 0) + 1
        # res = []
        # for key,value in freq.items():
        #     if value == 1:
        #         res.append(key)
        # return res
        freq = Counter((s1 + " " + s2).split())
        return [word for word, count in freq.items() if count == 1]

if __name__ == '__main__':
    s1 = "red blue"
    s2 = "red green"
    print(Solution().uncommonFromSentences(s1, s2))
