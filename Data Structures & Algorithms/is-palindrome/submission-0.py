class Solution:
    def isPalindrome(self, s: str) -> bool:
        for char in s:
            if not char.isalnum():
                s = s.replace(char, "")
        return list(reversed(s.lower())) == list(s.lower())