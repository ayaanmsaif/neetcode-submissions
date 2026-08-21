class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        if len(pattern) != len(s.split(" ")):
            return False 

        assigns = {}
        for i, word in enumerate(s.split(" ")):
            print(pattern[i])
            print(word)

            if word not in assigns.values():
                if pattern[i] not in assigns.keys(): 
                    assigns[pattern[i]] = word 
                else:
                    return False 

            if pattern[i] not in assigns.keys() and word in assigns.values():
                return False

        print(assigns)

        return True

