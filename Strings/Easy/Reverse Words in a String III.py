# Reverse the characters of every word in s. Keep the words in their original order and preserve the spaces separating
# them. Punctuation, digits, and other printable ASCII characters are part of their words.

class Solution:
    def reverseWords(self, s: str) -> str:
        #return ' '.join(word[::-1] for word in s.split())
        return ' '.join(map(lambda word:word[::-1], s.split()))
        # words = s.split()
        # ans = ""
        # for i in words:
        #     ans += i[::-1] + " "
        # return ans.strip()
        pass

if __name__ == '__main__':
    s = "ab cd"
    print(Solution().reverseWords(s))