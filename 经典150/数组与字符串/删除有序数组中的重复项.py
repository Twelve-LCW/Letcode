class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow=0
        n=len(nums)
        set=[]
        for fast in range(n):
            if nums[fast] not in set:
                set.append(nums[fast])
                nums[slow]=nums[fast]
                slow+=1
        return len(set)
    
class Solution:
    #严格递增：左边 < 右边。
    #非严格递增：左边 <= 右边。
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow