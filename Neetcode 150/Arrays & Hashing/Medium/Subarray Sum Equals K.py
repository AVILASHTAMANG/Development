# You are given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
#
# A subarray is a contiguous non-empty sequence of elements within an array.


# note : Reframe the problem using Prefix Sums
# Recall the definition of a prefix sum. Let P[j] be the sum of elements from index 0 to j:
#
# {sum}(nums[i \dots j]) = P[j] - P[i - 1]
# You want to find the number of index pairs $(i, j)$  such that:
#
# P[j] - P[i - 1] = k
# Rearrange that equation algebraically to isolate what you need from the past (P[i - 1]):
#
# P[i - 1] = P[j] - k
# The insight: As you iterate through the array and compute your current running sum (P[j]), you simply need to ask:
# “How many times in the past have I seen a prefix sum equal to (P[j] - k)?”


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # prefix = [0] * (n+1)
        # for i in range(n):
        #     prefix[i+1] = prefix[i] + nums[i]
        # count = 0
        # for start in range(n):
        #     for end in range(start, n):
        #         if prefix[end+1] - prefix[start] == k:
        #             count+=1
        # return count

        # above code is causing : Time Limit Exceeded. You may have an infinite loop or your code is too inefficient."
        count = 0
        curr_sum =0
        prefix_counts = {0:1} # think of it as marking(1) the starting point before taking the required step as before 1st element of array

        for num in nums:
            curr_sum += num
            if curr_sum-k in prefix_counts:
                count += prefix_counts[curr_sum-k] # It is answering: "How many valid subarrays end at this exact current position?"

            # Record/increment the current prefix sum frequency
            prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1
        return count


if __name__ == '__main__':
    nums = [2, -1, 1, 2]
    k = 2
    print(Solution().subarraySum(nums, k))