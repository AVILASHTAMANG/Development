# The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.
#
# For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
# You are given an array nums, return the sum of all XOR totals for every subset of nums.
#
# Note: Subsets with the same elements should be counted multiple times.
#
# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # O(2^n)
        total=0
        if not nums:
            return 0
        def backtrack(xor_val, i):
            nonlocal total
            if i==len(nums):
                total+=xor_val
                return
            backtrack(xor_val^nums[i],i+1)
            backtrack(xor_val, i+1)
        backtrack(0,0)
        return total

        # '''
        # Optimized — O(n):
        #
        # class Solution:
        #     def subsetXORSum(self, nums: List[int]) -> int:
        #         xor_all = 0
        #         for n in nums:
        #             xor_all |= n
        #         return xor_all << (len(nums) - 1)
        #
        # Why the O(n) works:
        #
        # Each bit that appears in any element is set in exactly 2^(n-1) subsets' XOR. So its contribution is 2^b × 2^(n-1).
        # Summing over all set bits = (OR of all elements) × 2^(n-1) = xor_all << (n-1).
        #
        # Sanity check with [1,2,3]:
        #
        # 1|2|3 = 3, 3 << 2 = 12 ✓
        # '''

if __name__=='__main__':
    nums=[2,4]
    print(Solution().subsetXORSum(nums))