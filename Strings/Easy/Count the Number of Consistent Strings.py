# You are given a string allowed consisting of distinct characters and an array of strings words.
# A string is consistent if all characters in the string appear in the string allowed.
#
# Return the number of consistent strings in the array words.

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allowed_set = set(allowed)
        for ch in words:
            # if set(ch) <= allowed_set:
            #     count += 1
            if all(c in allowed_set for c in ch):
                count += 1
        return count

if __name__ == '__main__':
    allowed = "ab"
    words = ["ad", "bd", "aaab", "baa", "badab"]
    print(Solution().countConsistentStrings(allowed, words))