# You are given a string s consisting of lowercase English letters.
#
# Your task is to find the maximum difference diff = freq(a1) - freq(a2) between the frequency of characters a1 and
# a2 in the string such that:
#
# a1 has an odd frequency in the string.
# a2 has an even frequency in the string.
# Return this maximum difference.

from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s).values()
        max_odd = max(n for n in counts if n%2 != 0)
        min_even = min(n for n in counts if n%2 == 0)
        return max_odd-min_even
        # freq = {}
        # for ch in s:
        #     freq[ch] = freq.get(ch, 0) + 1
        # max_odd = - 1
        # min_even = float('inf')
        # for val in freq.values():
        #     if val%2 != 0:
        #         max_odd= max(max_odd, val)
        #     else:
        #         min_even = min(min_even, val)
        # return (max_odd - min_even)

if __name__ == '__main__':
    s = "aabbbbccc"
    print(Solution().maxDifference(s))