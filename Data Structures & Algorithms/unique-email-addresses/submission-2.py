class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        cleaned = [] 
        atseen = False 
        plusseen = False 

        for email in emails:
            new = ""

            for char in email:
                
                if char == "@":
                    atseen = True 
                if atseen == False and char == ".":
                    continue 
                if char == "+":
                    plusseen = True
                if plusseen == True and atseen == False: 
                    continue 

                new += char 

            cleaned.append(new)
            atseen = False 
            plusseen = False 

        countEmails = Counter(cleaned)

        return len(countEmails)

            



