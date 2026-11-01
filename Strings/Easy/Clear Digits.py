# While s contains a digit, remove the leftmost digit together with the closest remaining letter to its left. Return the
# string after all digits have been removed. The input guarantees that a letter is available for every removal.

class Solution:
    def clearDigits(self, s: str) -> str:
        res = []
        for ch in s:
            if ch.isalpha():
                res.append(ch)
            else:
                res.pop()
        return ''.join(res)

if __name__ == '__main__':
    s = "abc123"
    print(Solution().clearDigits(s))