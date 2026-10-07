# You are given two strings order and s. All the characters of order are unique and were sorted in some custom
# order previously.
# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x
# occurs before a character y in order, then x should occur before y in the permuted string.
# Return any permutation of s that satisfies this property.


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq_s = {}
        ans = []
        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1
        for char in order:
            if char in s:
                ans.append(char * freq_s[char])
                # freq_s[char] = 0
                del freq_s[char]
        for char, count in freq_s.items():
            # if count>0:
            #     ans.append(char * count)
            ans.append(char * count)
        return ''.join(ans)


if __name__ == '__main__':
    order = "xabfcg"
    s = "agbfcdb"
    print(Solution().customSortString(order, s))
