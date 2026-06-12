class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # freq={}
        # for num in nums:
        #     freq[num] = freq.get(num,0) + 1
        #     if freq[num] >1 :
        #         return True
        # return False
        
        # Simpler solution
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
