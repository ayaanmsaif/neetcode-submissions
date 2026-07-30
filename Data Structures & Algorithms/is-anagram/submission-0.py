class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict() 
        dt = dict() 

        for char in s: 
            if char in d:
                d[char] += 1 
            else:
                d[char] = 1
            
        for char in t: 
            if char in dt:
                dt[char] += 1 
            else:
                dt[char] = 1

        if d == dt: 
            return True
        else:
            return False


