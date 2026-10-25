# Treat each of s and t as a sequence typed into its own initially empty editor. A lowercase letter appends that letter,
# and # removes the most recently entered letter if one exists. A backspace in an empty editor leaves it empty.
# # Return true if the two resulting texts are equal, and false otherwise.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # def build(text):
        #     stack = []
        #     for char in text:
        #         if char == '#':
        #             if stack:
        #                 stack.pop()
        #         else:
        #             stack.append(char)
        #     return ''.join(stack)
        #
        # return build(s) == build(t)

        ### reducing auxillary space form O(n+m) to O(1) ################
        i = len(s) - 1
        j = len(t) - 1
        while i>=0 or j>=0:
            skip_s = 0
            skip_t = 0
            while (i>=0):
                if s[i] == '#':
                    skip_s += 1
                    i -= 1
                elif skip_s>0:
                    skip_s -= 1
                    i -= 1
                else:
                    break

            while (j>=0):
                if t[j] == '#':
                    skip_t += 1
                    j -= 1
                elif skip_t>0:
                    skip_t -= 1
                    j -= 1
                else:
                    break
            if i>=0 and j>=0 and s[i]!=t[j]:
                return False
            if (i>=0) != (j>=0):
                return False

            i -= 1
            j -= 1
        return True

        pass

if __name__ == '__main__':
    s = "###"
    t = "a#"
    print(Solution().backspaceCompare(s, t))