class Solution:
    def jump(self, nums: List[int]) -> int:
        step=0
        boder=0
        maxpos=0
        n=len(nums)
        for i in range(n-1):
            maxpos=max(maxpos,i+nums[i])
            if i==boder:
                step+=1
                boder=maxpos
                if boder >= n - 1:
                    break
        return step