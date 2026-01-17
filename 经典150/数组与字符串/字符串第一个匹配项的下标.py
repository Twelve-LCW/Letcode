class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(haystack)
        l=len(needle)
        for i in range(n-l+1):
            if needle[0]==haystack[i]:
                if haystack[i:i+l]==needle:
                    return i
        return -1