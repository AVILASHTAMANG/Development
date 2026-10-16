# Choose two nonempty palindromic subsequences of s that use disjoint sets of character indices. Each subsequence
# preserves the original index order; the two choices may interleave, but they cannot share an index. A palindrome
# reads the same forward and backward. Return the largest possible product of the two subsequence lengths. You may
# leave characters unused.

class Solution:
    def maxProduct(self, s: str) -> int:

if __name__ == "_main__":
    s = "abcdef" # Output: 1
    print(Solution().maxProduct(s))