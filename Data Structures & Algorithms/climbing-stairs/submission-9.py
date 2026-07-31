class Solution:

    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2 or n == 3:
            return n

        ways = 1 
        i = 0 
        x = n - 1  
        y = 1 

        while i <= n//2: 
            ways += math.comb(x, y)
            x -= 1 
            y += 1 
            i += 1 
        
        return ways
        
        