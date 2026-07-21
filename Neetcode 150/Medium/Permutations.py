# Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.

from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path, remaining):
            if not remaining:
                res.append(path)
                return
            for i in range(len(remaining)):
                backtrack(path+[remaining[i]], remaining[:i]+remaining[i+1:])
        backtrack([],nums)
        return res

if __name__ == '__main__':
    nums = [1,2,3]
    print(Solution().permute(nums))
