# You are given an array nums of integers, which may contain duplicates. Return all possible subsets.
# The solution must not contain duplicate subsets. You may return the solution in any order.

from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(start,path):
            res.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()
        backtrack(0,[])
        return res


if __name__ == '__main__':
    nums = [1, 2, 1]
    print(Solution().subsetsWithDup(nums))
