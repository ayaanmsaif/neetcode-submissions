class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        o = [] 

        for i in range(len(arr)):

            if i != len(arr) - 1:
                greatest = max(arr[i+1:])
            else:
                break 
            
            o.append(greatest)


        o.append(-1)

        return o