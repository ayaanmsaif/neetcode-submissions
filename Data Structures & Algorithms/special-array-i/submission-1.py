class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        l = 0
        r = 1 

        if len(nums) == 1:
            return True

        while r <= len(nums) - 1 and l <= len(nums) -1  :

            if nums[l] % 2 == nums[r] % 2:
                return False

            l += 1
            r += 1

        return True
            