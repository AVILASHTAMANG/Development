# You are given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
#Could you do it in-place with O(1) extra space?

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k %= len(nums) # if k> len(nums)
        # nums[:] = nums[-k:] + nums[:-k] # nums[:] this replaces the nums list and rotates it to right
        # nums[:] = nums[k:] + nums[:k] # rotates to the left
        # return nums

        # above method rotates by using extra memory, whereas below one rotates in-place
        n = len(nums)
        k %= n
        def reverse(start, end):
            while start<end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0, n-1) # [8,7,6,5,4,3,2,1]
        reverse(0, k-1) # [5,6,7,8]
        reverse(k, n-1) # [1,2,3,4]
        # above gives right rotation

        # below is for left rotation
        # reverse(0, k-1)
        # reverse(k, n-1)
        # reverse(0, n-1)
        return nums


if __name__=='__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 4
    print(Solution().rotate(nums,k))