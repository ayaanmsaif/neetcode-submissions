class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        order_d = {}
        counts = Counter(s)
        string = ""

        for i, char in enumerate(order):
            if char in s:
                order_d[char] = i

        for key in order_d:
            
            for i in range(counts[key]):
                string += key

        for char in s:
            if char not in order:
                string += char

        return string

