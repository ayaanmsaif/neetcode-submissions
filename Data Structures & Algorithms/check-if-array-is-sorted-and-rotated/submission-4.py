class Solution:
    def check(self, nums: List[int]) -> bool:
        
        comp = nums.copy()
        comp.sort()

        for i in range(1, len(nums)+1):
            new = [] 
            
            for j in range(len(nums)):
                new.append(nums[(j+i) % len(nums)]) 

            if comp == new:
                return True 

        return False 