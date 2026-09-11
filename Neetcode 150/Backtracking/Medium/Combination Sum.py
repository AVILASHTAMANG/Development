# You are given an array of distinct integers nums and a target integer target. Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.
# The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.
# You may return the combinations in any order and the order of the numbers in each combination can be in any order.

from typing import List
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        if not nums:
            return []
        def backtrack(start,path,remaining):
            if remaining==0:
                res.append(path[:])
                return
            if remaining<0:
                return
            for i in range(start,len(nums)):
                if nums[i]>remaining:
                    break
                path.append(nums[i])
                backtrack(i,path,remaining-nums[i])
                path.pop()
        backtrack(0,[],target)
        return res

if __name__ == '__main__':
    nums = [2,5,6,9]
    target = 9
    print(Solution().combinationSum(nums,target))

