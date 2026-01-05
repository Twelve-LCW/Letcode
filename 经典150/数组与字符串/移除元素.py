class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res=0
        n=len(nums)
        for i in range(n):
            if nums[i]==val:
                nums[i]=101
                res+=1
        nums.sort()
        return res
    
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
    

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            if nums[left] == val:
                # 把右边的非 val 元素换过来
                nums[left] = nums[right]
                right -= 1
                # 注意：这里不 left += 1，因为换过来的元素还没检查！
            else:
                left += 1
                
        return left  # 或者 return right + 1