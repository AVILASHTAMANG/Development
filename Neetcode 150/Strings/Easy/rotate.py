class Solution:
    def rotate(self, s, n):
        n = n % len(s) #handle n > len(s)
        # return s[n:] +s[:n]
        return s[-n:] + s[:-n]

if __name__ == '__main__':
    s= "Avilash"
    n = 2
    print(Solution().rotate(s, n))