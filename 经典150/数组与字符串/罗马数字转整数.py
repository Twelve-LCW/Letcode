class Solution:
    def romanToInt(self, s: str) -> int:
        mp={}
        mp['I']=1
        mp['V']=5
        mp['X']=10
        mp['L']=50
        mp['C']=100
        mp['D']=500
        mp['M']=1000
        n=len(s)
        res=0
        for i in range(n-1,-1,-1):
            if i==n-1 or mp[s[i]]>=mp[s[i+1]]:
                res+=mp[s[i]]
            elif mp[s[i]]<mp[s[i+1]]:
                res-=mp[s[i]]
        return res