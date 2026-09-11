# You are given an integer array heights where heights[i] represents the height of the ith bar.
# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        start, end = 0, n-1
        maxarea=0
        while start<end:
            area = min(heights[start],heights[end])*(end-start)
            maxarea=max(maxarea,area)
            if heights[start]<heights[end]:
                start+=1
            else:
                end-=1
        return maxarea

if __name__=='__main__':
    height = [1, 7, 2, 5, 4, 7, 3, 6]
    print(Solution().maxArea(height))
