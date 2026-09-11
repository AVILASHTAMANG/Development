#Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
#A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.
#You must write an algorithm that runs in O(n) time.

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        for num in num_set:
            if num-1 not in num_set:
                curr_num = num
                length = 1
                while (curr_num+1) in num_set:
                    curr_num +=1
                    length += 1
                longest = max(longest,length)
        return longest

if __name__=='__main__':
    nums = [2,20,4,10,3,4,5]
    obj=Solution()
    print(obj.longestConsecutive(nums))

#this will return all the sequence as Lists
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> List[List[int]]:
#         sequences = []
#         num_set = set(nums)
#
#         for num in num_set:
#             # only start from beginning of a sequence
#             if num - 1 not in num_set:
#                 curr_num = num
#                 seq = [curr_num]
#
#                 while curr_num + 1 in num_set:
#                     curr_num += 1
#                     seq.append(curr_num)
#
#                 sequences.append(seq)
#
#         return sequences
