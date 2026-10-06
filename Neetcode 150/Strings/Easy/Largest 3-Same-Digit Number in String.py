# You are given a string num representing a large integer. An integer is good if it meets the following conditions:
#
# It is a substring of num with length 3.
# It consists of only one unique digit.
# Return the maximum good integer as a string or an empty string "" if no such integer exists.

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # char = ['999','888','777','666','555','444','333','222','111','000']
        # for i in range(len(char)):
        #     if char[i] in num:
        #         return char[i]
        max_good = ""
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                max_good = max(num[i:i+3], max_good)
        return max_good or ""




if __name__ == '__main__':
    num = "6777133339"
    print(Solution().largestGoodInteger(num))