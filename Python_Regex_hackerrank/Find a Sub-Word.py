# We define a word character to be any of the following:
#
# An English alphabetic letter (i.e., a-z and A-Z).
# A decimal digit (i.e., 0-9).
# An underscore (i.e., _, which corresponds to ASCII value ).
# We define a word to be a contiguous sequence of one or more word characters that is preceded and succeeded by one or
# more occurrences of non-word-characters or line terminators. For example, in the string I l0ve-cheese_?, the words are
# I, l0ve, and cheese_.
#
# We define a sub-word as follows:
#
# A sequence of word characters (i.e., English alphabetic letters, digits, and/or underscores) that occur in the same
# exact order (i.e., as a contiguous sequence) inside another word.
# It is preceded and succeeded by word characters only.
# Given  sentences consisting of one or more words separated by non-word characters, process  queries where each query
# consists of a single string, . To process each query, count the number of occurrences of  as a sub-word in all
# sentences, then print the number of occurrences on a new line.
#
# the pattern \Bcat\B will match the substring "cat" only if it is embedded within a larger word (like "catfish" or
# "certificate"), but it will not match if "cat" stands alone or is adjacent to non-word characters (like in "the cat"
# or "cat.").  Conversely, \b is used to match whole words only.

import re
class Solution:
    def count_subwords(self, sentences, queries):
        results = []

        for sentence in sentences:
            for query in queries:
                count = 0
                for word in re.findall(r'\w+', sentence):
                    count += len(re.findall(rf'(?={re.escape(query)})',word))
                results.append((sentence, query, count))
        return results

if __name__ == '__main__':
    sentences = [
        'existing pessimist optimist this is', 'atish missed his bus'
    ]
    queries = ['is']
    solution = Solution()
    for result in solution.count_subwords(sentences, queries):
        print(result)
