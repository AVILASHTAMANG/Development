# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of
# the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.
#
# You are also given an integer k, which is the desired number of consecutive black blocks.
#
# In one operation, you can recolor a white block such that it becomes a black block.
#
# Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # min_count = float('inf')
        # for i in range(len(blocks)-k+1):
        #     left = i
        #     count = 0
        #     while (left<i+k):
        #         if blocks[left] == 'W':
        #             count += 1
        #         left += 1
        #     min_count = min(min_count, count)
        # return min_count

        #Optimize using sliding window:
        count = blocks[:k].count('W')
        min_count = count
        for i in range(k, len(blocks)):
            if blocks[i-k] == 'W':
                count -= 1
            if blocks[i] == 'W':
                count += 1
            min_count = min(min_count, count)
        return min_count


if __name__=='__main__':
    # blocks = "WBBWWBBWBW" #O/P: 3
    # k = 7
    blocks = "WBWBBBW"
    k = 2
    print(Solution().minimumRecolors(blocks, k))