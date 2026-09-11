#Given an array of integers numbers that is sorted in non-decreasing order.
#Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
#There will always be exactly one valid solution.
#Your solution must use O(1) additional space.

from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers)-1
        while start<end:
            s = numbers[start]+numbers[end]
            if s==target:
                return [start+1,end+1]
            elif s>target:
                end-=1
            elif s<target:
                start+=1

if __name__=='__main__':
    obj = Solution()
    numbers = [1, 2, 3, 4]
    target = 3
    print(obj.twoSum(numbers,target))
