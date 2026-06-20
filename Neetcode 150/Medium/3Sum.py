#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
#The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-2):
            # Skip duplicates if i>0
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            start = i+1
            end = n-1
            while start<end:
                total = nums[i]+nums[start]+nums[end]
                if total == 0:
                    ans.append([nums[i], nums[start], nums[end]])
                    start+=1
                    end-=1
                    #skip duplicates for 2nd element
                    while start<end and nums[start]==nums[start-1]:
                        start+=1
                    #skip duplicates for 3rd element
                    while start<end and nums[end]==nums[end+1]:
                        end-=1
                elif total<0:
                    start+=1
                else:
                    end-=1
        return ans

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    obj = Solution()
    op = obj.threeSum(nums)
    print(op)