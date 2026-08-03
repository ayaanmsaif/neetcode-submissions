class Solution:
    def maxScore(self, s: str) -> int:
        zero_r = s.count("0") 
        one_r = s.count("1")

        zero_l = 0
        one_l = 0 

        max_score = -1 

        for i, num in enumerate(s):
            if i == len(s) - 1:
                break

            if num == '0':
                zero_l += 1 
                zero_r -= 1 
            
            if num == '1': 
                one_l += 1
                one_r -= 1 

            score = zero_l + one_r 

            if score > max_score: 
                max_score = score

        return max_score




        

        


            