class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 初始化：闭区间 [l, r]，搜索整个数组
        l, r = 0, len(nums) - 1
        
        # 闭区间标准循环：只要区间还有元素，就继续
        while l <= r:
            mid = (l + r) // 2  # 取中间位置
            
            # 核心判断：中间值 < 右边值
            if nums[mid] < nums[r]:
                # ✅ 说明：mid 到 r 这一段是【有序的】
                # 最小值一定在左边（包含 mid 自己）
                r = mid  # 保留 mid，缩小区间到左边
            else:
                # ❌ 说明：左边是更大的一段，最小值在右边
                # mid 不可能是最小值，直接抛弃
                l = mid + 1
        
        # 循环结束时 l > r，最小值就是 nums[r]
        return nums[r]