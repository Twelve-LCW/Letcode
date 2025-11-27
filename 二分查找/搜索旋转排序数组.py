class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first=nums[0]
        l,r=0,len(nums)-1
        if target<first:
            #目标值只能在后半部分
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]>target and nums[mid]<first:
                    r=mid-1
                else:
                    l=mid+1
        else:
            #目标值只能在前半部分
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target and nums[mid]>=first:
                    l=mid+1
                else:
                    r=mid-1
        return -1
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

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1