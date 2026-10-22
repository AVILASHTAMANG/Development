# A string can be shortened by replacing any number of non-adjacent, non-empty substrings with their lengths (without leading zeros).

# For example, the string "implementation" can be abbreviated in several ways, such as:

# "i12n" -> ("i mplementatio n")
# "imp4n5n" -> ("imp leme n tatio n")
# "14" -> ("implementation")
# "implemetation" -> (no substrings replaced)
# Invalid abbreviations include:

# "i57n" -> (i mplem entatio n, adjacent substrings are replaced.)
# "i012n" -> (has leading zeros)
# "i0mplementation" (replaces an empty substring)
# You are given a string named word and an abbreviation named abbr, return true if abbr 
# correctly abbreviates word, otherwise return false.

# A substring is a contiguous non-empty sequence of characters within a string.


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0

        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                # Leading zeros are invalid
                if abbr[j] == '0':
                    return False

                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1

                i += num

                # Number skips beyond the word
                if i > len(word):
                    return False

            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1

        return i == len(word) and j == len(abbr)


if __name__ == '__main__':
    word = "apple"
    abbr = "a3e"
    print(Solution().validWordAbbreviation(word, abbr))
