class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        ourbills = [] 
        first = False
        
        if bills[0] == 10 or bills[0] == 20:
            return False 

        for bill in bills:
            if bill == 5:
                ourbills.append(bill)

            if bill == 10:
                ourbills.append(bill) 
                if 5 not in ourbills:
                    return False 
                ourbills.remove(5)

            if bill == 20: 
                ourbills.append(20)
                if not ((ourbills.count(5) == 3) or (10 in ourbills and 5 in ourbills)): 
                    return False 

                if ourbills.count(5) >= 3:
                    first = True 
                    for i in range(3):
                        ourbills.remove(5)

                if first == False and 10 in ourbills and 5 in ourbills: 
                    ourbills.remove(10)
                    ourbills.remove(5)

                first = False 

        return True 
