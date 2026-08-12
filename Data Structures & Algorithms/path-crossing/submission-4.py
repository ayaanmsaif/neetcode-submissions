class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = [] 

        current = [0,0]
        cool = current.copy()
        visited.append(cool)

        for char in path:
            if char == "N":
                current[1] += 1 
            elif char == "S":
                current[1] -= 1
            elif char == "E":
                current[0] += 1 
            elif char == "W":
                current[0] -= 1

            coord = current.copy()
        
            if coord in visited:
                return True

            visited.append(coord)        
        return False 

        
