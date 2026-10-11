# You are given an array of integers nums, sort the array in ascending order and return it.
#
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with
# the smallest space complexity possible.

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Create a temporary array once to reuse during the merging process
        temp = [0] * len(nums)
        self.mergeSort(nums, temp, 0, len(nums) - 1)
        return nums

    def mergeSort(self, arr: List[int], temp: List[int], left: int, right: int) -> None:
        if left >= right:
            return

        mid = (left + right) // 2

        # Sort the left and right halves recursively
        self.mergeSort(arr, temp, left, mid)
        self.mergeSort(arr, temp, mid + 1, right)

        # Merge the sorted halves
        self.merge(arr, temp, left, mid, right)

    def merge(self, arr: List[int], temp: List[int], left: int, mid: int, right: int) -> None:
        # Copy the current section into the temporary array
        for i in range(left, right + 1):
            temp[i] = arr[i]

        i = left  # Pointer for the left subarray
        j = mid + 1  # Pointer for the right subarray
        k = left  # Pointer for the main array placement

        # Compare elements from both halves and merge them back in order
        while i <= mid and j <= right:
            if temp[i] <= temp[j]:
                arr[k] = temp[i]
                i += 1
            else:
                arr[k] = temp[j]
                j += 1
            k += 1

        # Copy any remaining elements from the left half (if any)
        while i <= mid:
            arr[k] = temp[i]
            i += 1
            k += 1

if __name__ == '__main__':
    nums = [10, 9, 1, 1, 1, 2, 3, 1]
    print(Solution().sortArray(nums))