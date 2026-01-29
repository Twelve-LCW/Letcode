class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]
        if not nums:
            return res
        start=nums[0]
        cur=nums[0]
        
        for i,num in enumerate(nums[1:]):
            if cur+1==num:
                cur=num
            else:
                if cur==start:
                    res.append(str(cur))
                else:
                    s=str(start)+"->"+str(cur)
                    res.append(s)
                start=num
                cur=num
        if cur==start:
            res.append(str(cur))
        else:
            s=str(start)+"->"+str(cur)
            res.append(s)
        return res

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i, n = 0, len(nums)
        while i < n:
            start = i
            while i < n - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            s = str(nums[start])
            if start < i:
                s += "->" + str(nums[i])
            ans.append(s)
            i += 1
        return ans