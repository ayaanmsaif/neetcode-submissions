class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_no = 0 
        count = 0 
        print(nums)

        for i, num in enumerate(nums):

            if num != 1:
                if count > max_no:
                    max_no = count
                count = 0 
            
            elif num == 1:
                count += 1    
             

            print("num: ",num)
            print("count ", count)

        if count > max_no:
            max_no = count

        return max_no 