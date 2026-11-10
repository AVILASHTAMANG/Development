# You are given an array nums, that might contain duplicates , return all possible unique permutations in any order.

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # high unrequired complexity
        # res=[]
        # def backtrack(path, remaining):
        #     if not remaining:
        #         if path not in res:
        #             res.append(path)
        #         return
        #     for i in range(len(remaining)):
        #         backtrack(path+[remaining[i]], remaining[:i]+remaining[i+1:])
        # backtrack([],nums)
        # return res

        res=[]
        nums.sort()
        used=[False]* len(nums)
        def backtrack(path):
            if len(path)==len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return res

if __name__=='__main__':
    nums = [1, 1, 2]
    print(Solution().permuteUnique(nums))