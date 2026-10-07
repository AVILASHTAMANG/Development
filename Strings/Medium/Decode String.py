# You are given an encoded string s, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is
# being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; there are no extra white spaces,
# square brackets are well-formed, etc. There will not be input like 3a, 2[4], a[a] or a[2].
#
# The test cases are generated so that the length of the output will never exceed 100,000.

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        current_num = 0
        for ch in s:
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)
            elif ch == '[':
                stack.append((current_string, current_num))
                current_string = ""
                current_num = 0
            elif ch == ']':
                prev_string, prev_num = stack.pop()
                current_string = prev_string + current_string * prev_num
            else:
                current_string += ch
        return current_string

if __name__=='__main__':
    s = "axb3[z]4[c]" # Output: "axbzzzcccc"
    print(Solution().decodeString(s))