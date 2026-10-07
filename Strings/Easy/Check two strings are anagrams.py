class Solution:
    def rotate(self, s1, s2):
        # return sorted(s1) == sorted(s2)
        freq1 = {}
        freq2 = {}
        for ch in s1:
            freq1[ch] = freq1.get(ch, 0) + 1
        for ch in s2:
            freq2[ch] = freq2.get(ch, 0) + 1
        return freq1 == freq2

if __name__ == '__main__':
    s1 = "Avilash"
    s2 = "hsalivA"
    print(Solution().rotate(s1, s2))  # True