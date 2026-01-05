class Solution(object):
    #暴力遍历
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[0,0]
        len_nums=len(nums)
        for i in range(0,len_nums):
            for j in range(i+1,len_nums):
                if nums[i]+nums[j]==target:
                    res[0]=i
                    res[1]=j
                    return res

#hashmap     
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashtable=dict()
        for i,num in enumerate(nums):
            if target-num in hashtable:
                return [hashtable[target-num],i]
            hashtable[nums[i]]=i
        return []