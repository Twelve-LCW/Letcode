class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        # 核心修改：循环条件改为 l < r，避免mid+1越界
        while l < r:
            mid = (l + r) // 2
            # 右边更大，峰值一定在右侧
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            # 左边更大，峰值一定在左侧
            else:
                r = mid
        return l