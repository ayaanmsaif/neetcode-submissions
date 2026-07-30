class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        d = dict()

        for num in nums:
            d[num] = 1 

        if len(d) < len(nums):
            return True

        return False