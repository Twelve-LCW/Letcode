class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_to_s={}
        s_to_p={}
        n=len(pattern)
        s=s.split(' ')
        if n!=len(s):
            return False

        for i in range(n):
            char_p=pattern[i]
            word_s=s[i]

            if word_s in s_to_p:
                if s_to_p[word_s]!=char_p:
                    return False
            else:
                s_to_p[word_s]=char_p


            if char_p in p_to_s:
                if p_to_s[char_p]!=word_s:
                    return False
            else:
                p_to_s[char_p]=word_s
        return True

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        n=len(pattern)
        s=s.split(' ')
        if n!=len(s):
            return False
        return len(set(zip(pattern,s)))==len(set(pattern))==len(set(s))