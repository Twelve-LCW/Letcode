class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(n-2):
            x=nums[i]
            if i>0 and x==nums[i-1]:
                continue
            if x+nums[i+1]+nums[i+2]>0:#当前剩下的组合中最小的都大于0，以后都找不到=0的了
                break
            if x+nums[-2]+nums[-1]<0: #这一轮最大的三个数都小于0，这一轮找不到=0的了
                continue
            l=i+1
            r=n-1
            while l<r:
                s=x+nums[l]+nums[r]
                if s>0:
                    r-=1
                elif s<0:
                    l+=1
                else:
                    if l==i+1 or nums[l]!=nums[l-1]:# j = i+1 表示刚开始双指针，此时 j 左边没有数字
                    # nums[j] != nums[j-1] 说明与上一轮循环的三元组不同
                        res.append([x,nums[l],nums[r]])
                    l+=1
                    r-=1
        return res