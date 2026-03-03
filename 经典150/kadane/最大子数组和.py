class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=nums[0]
        res=nums[0]
        for num in nums[1:]:
            s=max(s+num,num)
            res=max(res,s)
        return res
    
from typing import List

class Solution:    
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')  # 正确初始化（支持全负数）
        current_sum = 0
        left = 0
        
        for right in range(len(nums)):
            # 右指针扩展
            current_sum += nums[right]
            
            # 更新最大值
            max_sum = max(max_sum, current_sum)
            
            # 核心：如果当前窗口和 < 0，说明这个窗口不可能贡献更大值
            # 直接抛弃，left 跳到 right+1
            if current_sum < 0:
                current_sum = 0
                left = right + 1
        
        return max_sum