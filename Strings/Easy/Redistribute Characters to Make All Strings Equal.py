# You are given an array of strings words (0-indexed).
#
# In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character
# from words[i] to any position in words[j].
#
# Return true if you can make every string in words equal using any number of operations, and false otherwise.

from collections import Counter
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        char = ''.join(words)
        n = len(words)
        count = True
        freq = Counter(char)
        for key in freq:
            if freq[key] % n != 0:
                count = False
        return count

if __name__ == '__main__':
    words = ["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","abb","abb","abb","abb",
             "abb","abb","abb","abb","abb","abb","abb","abb","abb","abb","abb","abb","abb","abb","abb","abb"]
    print(Solution().makeEqual(words))