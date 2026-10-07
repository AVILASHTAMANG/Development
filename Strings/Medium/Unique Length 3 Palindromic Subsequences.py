# You are given a string s, return the number of unique palindromes of length three that are a subsequence of s.
#
# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
#
# A palindrome is a string that reads the same forwards and backwards.
#
# A subsequence of a string is a new string generated from the original string with some characters (can be none)
# deleted without changing the relative order of the remaining characters.
#
# For example, "ace" is a subsequence of "abcde".


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = {}
        last = {}
        for i in range(len(s)):
            char = s[i]
            if char not in first:
                first[char] = i
            last[char] = i

        ans = 0
        for char in first:
            left = first[char]
            right = last[char]

            if (right - left)>1:
                unique_middle_chars = set(s[left + 1 : right])

                #To return palindromic subsequence
                # for mid in unique_middle_chars:
                #     palindrome = f"{char}{mid}{char}"
                #     ans.append(palindrome)
                ans += len(unique_middle_chars)
        return ans


if __name__ == '__main__':
    s = "aabca"
    print(Solution().countPalindromicSubsequence(s))