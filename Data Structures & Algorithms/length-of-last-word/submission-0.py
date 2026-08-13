class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        c = s.split(" ") 

        what = []

        print(c)

        for i, char in enumerate(c):
            if char.isalpha():
                what.append(char)

        return len(what[-1])