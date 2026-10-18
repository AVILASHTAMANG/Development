# Return the starting indices of every substring of s that is an anagram of p. An anagram contains exactly the same
# letters with the same counts, possibly in a different order. Matching substrings may overlap. Indices are zero-based,
# and you may return them in any order.

from typing import List
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        f_p = Counter(p)
        k = len(p)
        f_s = Counter(s[:k]) # initialize first sliding window
        res = []
        # This below is correct as well , but the uncommented solution is better for large inputs as no COunter recalculation or new string slices are need to be created.
        # for i in range(len(s)-k+1):
        #     if f_p == Counter(s[i:(i+k)]):
        #         res.append(i)
        if f_s == f_p:
            res.append(0)
        for i in range(k, len(s)):
            f_s[s[i]] += 1
            outgoing = s[i-k]
            f_s[outgoing] -= 1
            if f_s[outgoing] == 0:
                del outgoing # don't want to count a:0 for example

            if f_p == f_s:
                res.append(i-k+1) # starting index
        return res



if __name__ == '__main__':
    s = "aaaa"
    p = "aa"
    print(Solution().findAnagrams(s, p)) # Output: [1,2]