class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0 
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            curr = nums[mid]

            if curr < target:
                l = mid + 1

            if curr > target:
                r = mid - 1

            if curr == target:
                return mid

        return -1 
                