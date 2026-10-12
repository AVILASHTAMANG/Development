# You are given a string array words, return an array of all characters that show up in all strings within the
# words (including duplicates). You may return the answer in any order.

# Input: words = ["bella","label","roller"]
#
# Output: ["e","l","l"]

from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        min_freq = [0] * 26
        for char in words[0]:
            min_freq[ord(char) - ord('a')] += 1

        for i in range(1, len(words)):
            current_freq = [0] * 26
            for char in words[i]:
                current_freq[ord(char) - ord('a')] += 1
            for j in range(26):
                min_freq[j] = min(current_freq[j], min_freq[j])
        result = []
        for j in range(26):
            if min_freq[j]>0:
                result.extend([chr(j + ord('a'))] * min_freq[j])
        return result


if __name__ == '__main__':
    words = ["cool", "lock", "cook"]
    print(Solution().commonChars(words))