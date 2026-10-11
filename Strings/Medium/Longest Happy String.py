# A string s is called happy if it satisfies the following conditions:
#
# s only contains the letters 'a', 'b', and 'c'.
# s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# s contains at most a occurrences of the letter 'a'.
# s contains at most b occurrences of the letter 'b'.
# s contains at most c occurrences of the letter 'c'.
# You are given three integers a, b, and c, return the longest possible happy string. If there are multiple longest
# happy strings, return any of them. If there is no such string, return the empty string "".
#
# A substring is a contiguous sequence of characters within a string.

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        counts = [[a,'a'], [b,'b'], [c,'c']]
        res = []
        while True:
            counts.sort(key=lambda x:x[0], reverse=True)
            added = False
            for i in range(len(counts)):
                count, char = counts[i]
                if count == 0:
                    break
                if len(res)>=2 and res[-1] == char and res[-2] == char:
                    continue
                res.append(char)
                counts[i][0] -= 1
                added = True
                break
            if not added:
                break
        return ''.join(res)




if __name__ == '__main__':
    a = 0
    b = 1
    c = 5
    print(Solution().longestDiverseString(a, b, c))