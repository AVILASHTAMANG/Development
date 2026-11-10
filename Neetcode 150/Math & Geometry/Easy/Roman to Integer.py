# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# You are given a roman numeral as a string s, convert it to an integer.
#

# Hint : Because of the Roman numeral subtraction rule: a smaller value placed before a larger one means subtract it.
#
# IV = 4  (I is before V → I is subtracted)
# VI = 6  (I is after V  → I is added)
# Why -2× and not -1×? Because you need to both remove the +prev_val you already added, and apply the correct -prev_val.
# That's two subtractions of prev_val.

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        res = 0
        prev_val = 0
        for ch in s:
            if roman_values[ch]>prev_val:
                res+= roman_values[ch]-2*prev_val
            else:
                res+=roman_values[ch]
            prev_val=roman_values[ch]
        return res

if __name__=='__main__':
    s = "XLIX"
    print(Solution().romanToInt(s))