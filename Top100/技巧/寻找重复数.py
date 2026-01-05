class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=fast=0 #不在环上，可以作为起点
        while True:
            slow=nums[slow] #等价于slow=slow.next
            fast=nums[nums[fast]] #等价于fast=fast.next.next
            if fast==slow:
                break
        head=0
        while head!=slow:
            head=nums[head]
            slow=nums[slow]
        return slow

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = [0] * len(nums)
        for num in nums:
            if ans[num]:
                return num
            else:
                ans[num] = 1