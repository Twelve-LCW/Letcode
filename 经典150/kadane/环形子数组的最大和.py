class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        
        # 求最大子数组和（不跨环）
        cur_max = max_sum = nums[0]
        # 求最小子数组和（跨环时用：总和 - 最小和）
        cur_min = min_sum = nums[0]
        
        for num in nums[1:]:
            # 最大
            cur_max = max(num, cur_max + num)
            max_sum = max(max_sum, cur_max)
            
            # 最小
            cur_min = min(num, cur_min + num)
            min_sum = min(min_sum, cur_min)
        
        # 特殊情况：全是负数，直接返回 max_sum
        if max_sum < 0:
            return max_sum
        
        # 答案 = max(不跨环最大, 跨环最大(total - min_sum))
        return max(max_sum, total - min_sum)