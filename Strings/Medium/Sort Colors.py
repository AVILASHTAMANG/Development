# You are given an array nums consisting of n elements where each element is an integer representing a color:
#
# 0 represents red
# 1 represents white
# 2 represents blue
# Your task is to sort the array in-place such that elements of the same color are grouped together and arranged in
# the order: red (0), white (1), and then blue (2).
#
# You must not use any built-in sorting functions to solve this problem.

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ##### QuickSort method ###########
        def quicksort(arr, low, high):
            if low < high:
                pivot_idx = partition(arr, low, high)
                quicksort(arr, low, pivot_idx - 1)
                quicksort(arr, pivot_idx + 1, high)

        def partition(arr, low, high):
            pivot = arr[high] # Choose the last element as pivot
            i = low - 1 # Index of smaller element
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        if nums:
            quicksort(nums, 0, len(nums) - 1)

        #Dutch National Flag ($O(n)$ One-Pass)
        # Use three pointers to partition the array into three zones:
        # low: Boundary for 0s (everything before low is 0)
        # mid: Current element being inspected
        #
        # high: Boundary for 2s (everything after high is 2)

        low = 0
        mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid]==0:
                nums[low], nums[mid] = nums[mid], nums[low]
                mid += 1
                low += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                # Note: Do not increment mid here because the swapped
                # element from nums[high] has not been evaluated yet.



if __name__ == '__main__':
    solution = Solution()
    nums = [1, 0, 1, 2]
    solution.sortColors(nums)
    print(nums)  # Output: [0, 1, 1, 2]
