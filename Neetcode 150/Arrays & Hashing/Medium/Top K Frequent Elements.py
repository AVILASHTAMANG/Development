# Given an integer array nums and an integer k, return the k most frequent elements within the array.
#
# The test cases are generated such that the answer is always unique.
#
# You may return the output in any order.

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count = Counter(nums)
        # return [num for num, _ in sorted(count.items(), key=lambda x: x[1], reverse=True)[:k]] ##(O) nlogn
        freq = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)
        result = []
        for count in range(len(buckets)-1,0,-1):
            for num in buckets[count]:
                result.append(num)
                if len(result) == k:
                    return result


if __name__ == '__main__':
    nums = [1, 2, 2, 3, 3, 3]
    k = 2
    print(Solution().topKFrequent(nums, k))

