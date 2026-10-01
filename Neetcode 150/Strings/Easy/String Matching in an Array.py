# You are given an array of string words, return all strings in words that are a substring of another word. You
# can return the answer in any order.
# Note: A substring is a contiguous non-empty sequence of characters within a string.

from typing import List
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        #return [w for w in words if any(w in other and w != other for other in words)]

        #without using built-in methods # helper function
        def find_substring(text, sub):
            for i in range(len(text) - len(sub) + 1):
                match = True
                for j in range(len(sub)):
                    if text[i+j] != sub[j]:
                        match = False
                        break
                if match:
                    return i
            return  -1

        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and find_substring(words[j], words[i]) != -1:
                    res.append(words[i])
                    break
        return res

if __name__ == '__main__':
    words = ["mass", "as", "hero", "superhero"]
    print(Solution().stringMatching(words))