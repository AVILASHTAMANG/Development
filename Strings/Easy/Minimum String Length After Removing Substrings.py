# Starting with the uppercase string s, repeatedly delete any adjacent AB or CD. The characters on either side join
# together after a deletion, which may allow more deletions. Return the shortest length you can obtain, including zero
# if everything can be removed.

class Solution:
    def minLength(self, s: str) -> int:
        pass
        res = []
        for ch in s:
            if res and ((res[-1]=='A' and ch =='B') or (res[-1]=='C' and ch=='D')):
                res.pop()
            else:
                res.append(ch)
        return len(res)

if __name__=='__main__':
    s = "AB"
    print(Solution().minLength(s))