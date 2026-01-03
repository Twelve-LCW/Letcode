class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        lim=threshold*k
        s=sum(arr[:k])
        res=1 if s>=lim else 0
        for i in range(k,len(arr)):
            s+=arr[i]-arr[i-k]
            res+=1 if s>=lim else 0
        return res