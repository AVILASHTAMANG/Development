# Scan words from left to right and return the first word whose letters match when read in reverse order. If no word
# meets this condition, return the empty string "".

from typing import List
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""

if __name__=='__main__':
    words = ["desk", "level", "noon"] #Output: "level"
    print(Solution().firstPalindrome(words))