# We define a word as a non-empty maximum sequence of characters that can contain only lowercase letters,
# uppercase letters, digits and underscores '_' (ASCII value 95). Maximum sequence means that the word has to be
# immediately preceeded by a character not allowed to occur in a word or by the left boundary of the sentence, and
# it has to be immediately followed by a character not allowed to occur in a word or by the right boundary of the
# sentence.
# For every word, print the number of occurrences of the word in all the sentence listed.


import re

class Solution:
    def find_word(self, sentence):
        word = "foo"
        regex_pattern = r'(?<![a-zA-Z0-9_])' + re.escape(word) + r'(?![a-zA-Z0-9_])'
        return len(re.findall(regex_pattern, sentence))

if __name__ == '__main__':
    sentence = "foo bar (foo) bar foo-bar foo_bar foo'bar bar-foo bar, foo."
    print(Solution().find_word(sentence))


