# You are given two strings, word1 and word2. Construct a new string by merging them in alternating order, 
# starting with word1 — take one character from word1, then one from word2, and repeat this process.

# If one string is longer than the other, append the remaining characters from the longer string to the 
# end of the merged result.

# Return the final merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i = 0
        while i<len(word1) or i<len(word2):
            if i<len(word1):
                res.append(word1[i])
            if i<len(word2):
                res.append(word2[i])
            i += 1
        return ''.join(res)

if __name__ == '__main__':
    word1 = "ab"
    word2 = "abbxxc"
    print(Solution().mergeAlternately(word1, word2))
