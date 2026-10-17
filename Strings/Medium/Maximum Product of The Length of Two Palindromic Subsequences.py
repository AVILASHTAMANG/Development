# Choose two nonempty palindromic subsequences of s that use disjoint sets of character indices. Each subsequence
# preserves the original index order; the two choices may interleave, but they cannot share an index. A palindrome
# reads the same forward and backward. Return the largest possible product of the two subsequence lengths. You may
# leave characters unused.

from typing import List
# class Solution:
#     def maxProduct(self, s: str) -> int:
#         # Method 1 : Bitwise Precomputation : This approach precomputes all valid palindromic subsequences by
#         checking each bitmask from $1$ to $2^n - 1$, then checks all pairs of masks to find the maximum product
#         of disjoint pairs.
#
#         n = len(s)
#         palindrome = {} # mask:key
#
#         # Generate all possible subsequences and their lengths
#         for mask in range(1, 1<<n):
#             subseq = [s[i] for i in range(n) if (mask >> i) & 1]
#             if subseq == subseq[::-1]:
#                 palindrome[mask] = len(subseq)
#
#         # Verify every pair of disjoint palindromes
#         max_prod = 0
#         pal_items = list(palindrome.items())
#         total_pals = len(pal_items)
#         for i in range(total_pals):
#             mask1, len1 = pal_items[i]
#             if len1 * (n - len1) <= max_prod: # Optimization
#                 continue
#             for j in range(i+1, total_pals):
#                 mask2, len2 = pal_items[j]
#                 if (mask1 & mask2) == 0: # disjoint check
#                     max_prod = max(max_prod, len1 * len2)
#
#         return max_prod


class Solution:
    def maxProduct(self, s: str) -> int:
#         # Method 2 : 3-Way Backtracking(DFS) with Pruning At each index $i$, character $s[i]$ can either go to
#         subsequence 1, subsequence 2, or be skipped. A mathematical upper-bound check prunes branches that cannot
#         possibly beat the best product found so far.
        n = len(s)
        self.max_prod = 0
        s1 = []
        s2 = []
        

        def is_palindrome(chars: list[str]) -> bool:
            l, r = 0, len(chars) - 1
            while l < r:
                if chars[l] != chars[r]:
                    return False
                l += 1
                r -= 1
            return True


        def dfs(i: int):
            # Pruning: The maximum possible product of two numbers summing to S
            # occurs when they are split as equally as possible: floor(S/2) * ceil(S/2).
            remaining = n - i
            total_possible_chars = len(s1) + len(s2) + remaining
            max_possible_prod = (total_possible_chars // 2) * ((total_possible_chars + 1) // 2)

            if max_possible_prod <= self.max_prod:
                return

            # Base case: evaluated all characters
            if i == n:
                if is_palindrome(s1) and is_palindrome(s2):
                    self.max_prod = max(self.max_prod, len(s1) * len(s2))
                return

            # Branch 1: Add s[i] to sequence 1
            s1.append(s[i])
            dfs(i + 1)
            s1.pop()

            # Branch 2: Add s[i] to sequence 2
            s2.append(s[i])
            dfs(i + 1)
            s2.pop()

            # Branch 3: Leave s[i] unused
            dfs(i + 1)


        dfs(0)
        return self.max_prod


if __name__ == '__main__':
    s = "abcdef" # Output: 1
    print(Solution().maxProduct(s))