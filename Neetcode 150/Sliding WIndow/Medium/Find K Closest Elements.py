# You are given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The
# result should also be sorted in ascending order.
#
# An integer a is closer to x than an integer b if:
#
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = k
        while right<len(arr):
            if x - arr[left] > arr[right] - x:
                left+=1
                right+=1
            else:
                break
        return arr[left:left+k]

if __name__=='__main__':
    arr = [2, 4, 5, 8]
    k = 2
    x = 6
    print(Solution().findClosestElements(arr,k,x))
