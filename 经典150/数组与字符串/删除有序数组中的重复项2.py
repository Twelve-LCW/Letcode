class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        stack_size=2
        for i in range(2,len(nums)):
            if nums[i]!=nums[stack_size-2]:
                nums[stack_size]=nums[i]
                stack_size+=1
        return min(stack_size,len(nums))
    
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        slow,fast,idx = 1,1,1
        val = nums[0]
        while fast < len(nums):
            if idx == 0:
                val = nums[fast]
            if nums[fast] != val:
                idx = 0
                continue
            if idx < 2 and nums[fast] == val:
                idx += 1
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
                
    
        