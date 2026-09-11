# Given an array nums of unique integers, return all possible subsets of nums.
# The solution set must not contain duplicate subsets. You may return the solution in any order.

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start,path):
            res.append(path[:])
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()
        backtrack(0,[])
        return res

if __name__ == '__main__':
    nums = [1,2,3]
    print(Solution().subsets(nums))



