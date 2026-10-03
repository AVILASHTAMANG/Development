# A distinct string is a string that is present only once in an array.
#
# You are given an array of strings arr, and an integer k, return the k-th distinct string present in arr.
# If there are fewer than k distinct strings, return an empty string "".
#
# Note that the strings are considered in the order in which they appear in the array.

from typing import List
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}
        for ch in arr:
            freq[ch] = freq.get(ch, 0) + 1
        #ans = []
        for ch in arr:
            if freq[ch] == 1:
                # ans.append(ch)
                k -= 1
                if k == 0:
                    return ch
        # if len(ans)<k:
        #     return ""
        # return ans[k-1]
        return ""


if __name__ == '__main__':
    arr = ["d", "b", "c", "b", "c", "a"]
    k = 2
    print(Solution().kthDistinct(arr, k))

