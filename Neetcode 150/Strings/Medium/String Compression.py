# You are given an array of characters chars, compress it using the following algorithm:
#
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
#
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
# Note that group lengths that are 10 or longer will be split into multiple characters in chars. For example,
# 10 is represented as ["1","0"].
#
# Let k be the length of the compressed string s. You must modify the first k characters of chars array and return k.
#
# You must write an algorithm that uses only constant extra space.

from collections import Counter
from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        while read < len(chars):
            char = chars[read]
            anchor = read
            while (read < len(chars) and chars[read] == char):
                read += 1
            chars[write] = char
            write += 1
            length = read - anchor
            if length > 1:
                for ch in str(length):
                    chars[write] = ch
                    write += 1
        return write

if __name__ == '__main__':
    chars = ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
    print(Solution().compress(chars))
