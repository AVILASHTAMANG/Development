# You are given an array of characters which represents a string s. Write a function which reverses a string.
#
# You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

if __name__ == '__main__':
    s = ["n","e","e","t"]
    Solution().reverseString(s)
    print(s)
