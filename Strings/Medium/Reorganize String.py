# You are given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
#
# You can return any possible rearrangement of s or return "" if not po ssible.

from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        # counts = {}
        # for char in s:
        #     counts[char] = counts.get(char, 0) + 1
        # sorted_chars = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
        # most_frequent_char = sorted_chars[0]
        # if counts[most_frequent_char] > (len(s) + 1) // 2:
        #     return ""

        count = Counter(s)
        most_common = count.most_common()
        if most_common[0][1] > (len(s)+1) // 2:
            return ""
        idx = 0
        res = len(s) * [""]
        for char, freq in most_common:
            for _ in range(freq):
                res[idx] = char
                idx += 2
                if idx >= len(s):
                    idx = 1
        return ''.join(res)

if __name__ == '__main__':
    s = "abbccdd"
    print(Solution().reorganizeString(s))   # "abcdbcd"