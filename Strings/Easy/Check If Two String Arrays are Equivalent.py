# Concatenate the strings in word1 in their given order, and do the same for word2. Return true if the two resulting
# strings are identical, or false otherwise. The boundaries between the individual pieces do not affect the comparison.

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return (''.join(word1)==''.join(word2))

if __name__ == '__main__':
    word1 = ["ne", "et"]
    word2 = ["n", "eet"]
    print(Solution().arrayStringsAreEqual(word1,word2)) #o/p: true