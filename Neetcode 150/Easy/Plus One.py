# You are given an integer array digits, where each digits[i] is the ith digit of a large integer. It is ordered from most significant to least significant digit, and it will not contain any leading zero.
# Return the digits of the given integer after incrementing it by one.

from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)-1
        while n>=0:
            if digits[n]<9:
                digits[n]+=1
                return digits
            digits[n]=0
            n-=1
        return [1]+ digits

if __name__=="__main__":
    digits = [1, 2, 3, 4]
    print(Solution().plusOne(digits))
