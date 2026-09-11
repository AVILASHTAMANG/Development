# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
# Each product is guaranteed to fit in a 32-bit integer.
# Follow-up: Could you solve it in O(n) time without using the division operation?
# Example 1:
# Input: nums = [1,2,4,6]
# Output: [48,24,12,8]

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute force :
        # n = len(nums)
        # result=[]
        # for i in range(n):
        #     product = 1
        #     for j in range(n):
        #         if i!=j:
        #             product *= nums[j]
        #     result.append(product)
        # return result

        #using prefix and suffix technique
        n = len(nums)
        result = [1] * n
        # prefix product
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        #suffix product
        suffix = 1
        for i in range(n-1,-1,-1):
            result[i] *= suffix
            suffix *= nums[i]
        return result

if __name__ == '__main__':
    nums = [1,2,4,6]
    obj = Solution()
    op = obj.productExceptSelf(input)
    print(op)

