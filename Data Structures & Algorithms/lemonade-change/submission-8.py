class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        wallet = {5:0, 10:0, 20:0}
        first_op = False 

        if bills[0] == 10 or bills[0] == 20:
            return False

        for bill in bills:
            if bill == 5:
                wallet[5] += 1 

            if bill == 10: 
                wallet[10] += 1
                if wallet[5] <= 0:
                    return False 
                wallet[5] -= 1 

            if bill == 20: 
                wallet[20] += 1 
                print(wallet)

                if (wallet[5] < 3) and (wallet[10] < 1 or wallet[5] < 1): 
                    return False 

                if wallet[5] >= 3:
                    first_op = True 
                    wallet[5] -= 3 

                if first_op == False and (wallet[10] >= 1 and wallet[5] >= 1):
                    wallet[10] -= 1
                    wallet[5] -= 1

            first_op = False

        return True
                


            

        
        