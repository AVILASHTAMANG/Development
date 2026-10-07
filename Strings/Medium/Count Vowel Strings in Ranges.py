# You are given a 0-indexed array of strings words and a 2D array of integers queries.
#
# Each query queries[i] = [li, ri] asks us to find the number of strings present at the indices ranging from li to ri
# (both inclusive) of words that start and end with a vowel.
#
# Return an array ans of size queries.length, where ans[i] is the answer to the i-th query.
#
# Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

from typing import List
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n =  len(words)
        valid_words = [0] * (n+1)
        for i in range(n):
            is_valid = 1 if words[i][0] in vowels and words[i][-1] in vowels else 0
            valid_words[i + 1] = valid_words[i] + is_valid
        ans = []
        for l,r in queries:
            ans.append(valid_words[r+1] - valid_words[l])
        return ans
        # vowels = {'a', 'e', 'i', 'o', 'u'}
        # ans = []
        #
        # for l, r in queries:
        #     count = 0
        #     for i in range(l, r + 1):
        #         if words[i][0] in vowels and words[i][-1] in vowels:
        #             count += 1
        #     ans.append(count)
        # return ans

if __name__=='__main__':
    words = ["aba", "bcb", "ece", "aa", "e"]
    queries = [[0, 2], [1, 4], [1, 1]]
    print(Solution().vowelStrings(words, queries))