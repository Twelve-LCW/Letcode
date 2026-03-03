class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = -1, len(nums) - 1  # 开区间 (-1, n-1)
        while left + 1 < right:  # 开区间不为空
            mid = (left + right) // 2
            x = nums[mid]
            if target > nums[-1] >= x:  # target 在第一段，x 在第二段
                right = mid  # 下轮循环去左边找
            elif x > nums[-1] >= target:  # x 在第一段，target 在第二段
                left = mid  # 下轮循环去右边找
            elif x >= target:  # 否则，x 和 target 在同一段，这就和方法一的 lower_bound 一样了
                right = mid
            else:
                left = mid
        return right if nums[right] == target else -1


from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 闭区间标准初始化：搜索范围是 [0, len(nums)-1]，覆盖整个数组
        left, right = 0, len(nums) - 1
        
        # 闭区间标准循环条件：只要区间不为空，就继续搜索
        while left <= right:
            # 计算中间位置，防止越界的标准写法
            mid = (left + right) // 2
            x = nums[mid]  # 简化变量，方便阅读
            
            # 一、如果已经找到目标，直接返回下标（闭区间常用写法）
            if x == target:
                return mid

            # ==============================================
            # 下面逻辑：处理【旋转排序数组】的两段式特性
            # 数组分成：左段（大数）、右段（小数）
            # nums[-1] 是数组最后一个数，用来区分两段
            # ==============================================

            # 情况1：target 在左段，mid 在右段
            # 说明答案一定在 mid 左边
            if target > nums[-1] >= x:
                right = mid - 1  # 闭区间：去左边，必须 -1

            # 情况2：mid 在左段，target 在右段
            # 说明答案一定在 mid 右边
            elif x > nums[-1] >= target:
                left = mid + 1   # 闭区间：去右边，必须 +1

            # 情况3：mid 和 target 在【同一段】
            # 退化成普通有序数组二分查找
            elif x >= target:
                # 比目标大，去左边找
                right = mid - 1
            else:
                # 比目标小，去右边找
                left = mid + 1

        # 跳出循环 = 遍历完没找到，返回 -1
        return -1