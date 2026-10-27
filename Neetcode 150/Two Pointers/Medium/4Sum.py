# You are given an integer array nums of size n, return an array of all the unique quadruplets [nums[a], nums[b],
# nums[c], nums[d]] such that:
#
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.
#
# Note: [1,0,3,2] and [3,0,1,2] are considered as same quadruplets.

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        if len(nums)<4:
            return res
        for i in range(n-3): # fixing first element nums[i]
            if i > 0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j>i+1 and nums[j]==nums[j-1]: # fixing the 2nd element
                    continue
                start = j+1 # fixing 3rd element
                end = n-1 # fixing 4th element
                while start<end:
                    curr_sum = nums[i]+nums[j]+nums[start]+nums[end]
                    if curr_sum==target:
                        res.append([nums[i],nums[j],nums[start],nums[end]])

                        # skip duplicate for 3rd element
                        while (start<end and nums[start]==nums[start+1]):
                            start += 1

                        # skip duplicate for 4th element
                        while (start<end and nums[end]==nums[end-1]):
                            end -= 1
                        start += 1
                        end -= 1
                    elif curr_sum<target:
                        start += 1
                    else:
                        end -= 1
        return res



if __name__=='__main__':
    # nums = [3, 2, 3, -3, 1, 0]
    # target = 3
    # Output: [[-3,0,3,3],[-3,1,2,3]]

    nums = [2, 2, 2, 2, 2]
    target = 8
    print(Solution().fourSum(nums,target))

