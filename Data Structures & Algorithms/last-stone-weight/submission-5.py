class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones.sort(reverse=True)

        while len(stones) > 1: 
            print(stones)
            
            if stones[0] == stones[1]:
                stones.pop(0)
                stones.pop(0)

            elif stones[0] < stones[1]:
                x = stones.pop(0)
                stones[0] = stones[0] - x 

            elif stones[1] < stones[0]:
                y = stones.pop(1)
                stones[0] = stones[0] - y  

            stones.sort(reverse=True)

        if stones:
            return stones[0]
        else:
            return 0 