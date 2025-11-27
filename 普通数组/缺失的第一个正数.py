class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        res=1
        n=len(nums)
        if nums[0]>1 or nums[n-1]<=0:
            return res
        pos=-1
        for i in range(n):
            if nums[i]>0:
                pos=i
                break
        nums=nums[pos:]
        for i in range(1,n-pos+2):
            if i==n-pos+1:
                res=n-pos+1
                break
            elif i!=nums[i-1]:
                res=i
                break
        return res        


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        # 求出在1~len(nums)中没有出现的最小正数
        # 创建长度为len(nums)+1的新数组，遍历nums，把范围内的num放在一个新数组的num下标位置
        # 遍历新数组，找出第一个值不等于下标的，返回下标
        n = len(nums)
        new_nums = [0]*(n+1)
        for i in nums:
            if 1 <= i and i <= n:
                new_nums[i] = i
        for i in range(1,n+1):
            if new_nums[i] != i:
                return i
        # 如果新数组都被正确填满，返回n+1
        return n+1