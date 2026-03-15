class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        num_set=set(nums)  # 把 nums 转成哈希集合
        for num in num_set:
            if num-1 in num_set: # 如果 x 不是序列的起点，直接跳过
                continue

            cur_num=num
            while cur_num+1 in num_set: # 不断查找下一个数是否在哈希集合中
                cur_num+=1
            res=max(cur_num-num+1,res)
        return res