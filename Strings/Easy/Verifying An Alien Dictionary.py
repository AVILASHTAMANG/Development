# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order.
# The order of the alphabet is some permutation of lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of the alphabets, return true if and only if
# the given words are sorted lexicographically in this alien language.

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {char:index for index,char in enumerate(order)}

        for i in range(len(words)-1):
            word1=words[i]
            word2=words[i+1]
            for j in range(min(len(word1), len(word2))):
                if word1[j]!=word2[j]:
                    if order_dict[word1[j]]>order_dict[word2[j]]:
                        return False
                    break
            else:
                if len(word1)>len(word2):
                    return False
        return True

if __name__=='__main__':
    words = ["neetcode", "neet"]
    order = "worldabcefghijkmnpqstuvxyz"
    print(Solution().isAlienSorted(words,order ))
