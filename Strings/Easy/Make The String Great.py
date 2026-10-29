# Repeatedly remove an adjacent pair when the characters are the same English letter in opposite cases, such as aA or Bb.
# Continue until no such pair remains and return the resulting string. The result is unique; an empty result is allowed.

class Solution:
    def makeGood(self, s: str) -> str:
        res=[]
        for c in s:
            if res and abs(ord(c) - ord(res[-1])) == 32:
                res.pop()
            else:
                res.append(c)
        return ''.join(res)
        pass

if __name__ == '__main__':
    s = "abBA"
    print(Solution().makeGood(s))