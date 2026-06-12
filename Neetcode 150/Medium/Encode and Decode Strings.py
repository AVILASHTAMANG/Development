# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s))+"#"+s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i=0
        while(i<len(s)):
            j=i
            while(s[j]!="#"):
                j+=1
            length=int(s[i:j])
            word = s[j+1:j+1+length]
            decoded.append(word)
            i=j+1+length
        return decoded

if __name__== '__main__':
    strs = ["Hello","World"]
    obj = Solution()
    res = obj.encode(strs)
    print(res)
    ans = obj.decode(res)
    print(ans)