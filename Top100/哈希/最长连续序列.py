class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=1
        nums.sort()
        leng=len(nums)
        max_len=1
        if leng==0:
            return 0
        for i in range(0,leng-1):
            if nums[i]+1==nums[i+1]:
                max_len+=1
            elif nums[i]==nums[i+1]:
                max_len+=0
            else:
                max_len=1
            res=max(res,max_len)
        return res
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len=0
        num_set=set(nums)
        for num in num_set:
            if num-1 not in num_set:
                current_num=num
                current_len=1

                while current_num+1 in num_set:
                    current_num+=1
                    current_len+=1
                max_len=max(max_len,current_len)
        return max_len