# You are given a string sentence containing English words separated by spaces.
#
# Treat the words as a circle: each word must end with the character that starts the following word, including the
# connection from the final word back to the first. Return true when every connection matches, or false otherwise.
# Comparisons are case-sensitive.

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                if sentence[i-1] != sentence[i+1]:
                    return False
        return sentence[0] == sentence[-1]

if __name__ == '__main__':
    sentence = "ab ca"
    print(Solution().isCircularSentence(sentence))
