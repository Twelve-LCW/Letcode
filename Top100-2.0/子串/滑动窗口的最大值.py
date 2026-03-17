import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        if  not nums or k==0 or n<k: return []
        deque=collections.deque()
        for i in range(k):
            while deque and deque[-1]<nums[i]:
                deque.pop()
            deque.append(nums[i])
        res=[deque[0]]
        for i in range(k,n):
            if deque[0]==nums[i-k]:
                deque.popleft()
            while deque and deque[-1]<nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res