# You are given a string text, you want to use the characters of text to form as many instances of the word
# "balloon" as possible.
#
# You can use each character in text at most once. Return the maximum number of instances that can be formed.

from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # freq = {}
        # for ch in text:
        #     freq[ch] = freq.get(ch, 0) + 1

        # max_balloon = float('inf')
        # letters = ["b", "a", "l", "o", "n"]
        #
        # for letter in letters:
        #     if letter not in freq:
        #         return 0
        #     # if letter in ("l", "o") and (freq[letter] < 1) :
        #     #     return 0
        #     if letter in ("l", "o"):
        #         freq[letter] = freq[letter] // 2
        #     max_balloon = min(freq[letter], max_balloon)
        # return max_balloon

        # built-in method , faster
        freq = Counter(text)
        return min(
            freq['b'],
            freq['a'],
            freq['l'] // 2,
            freq['o'] // 2,
            freq['n']
        )

if __name__ == '__main__':
    #text = "loonbalxballpoon"
    text= "balon"
    print(Solution().maxNumberOfBalloons(text))
