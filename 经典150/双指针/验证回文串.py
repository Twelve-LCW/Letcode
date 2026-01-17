class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= ''.join(ch for ch in s if ch.isalnum())
        s=s.lower()
        return True if s==s[::-1] else False