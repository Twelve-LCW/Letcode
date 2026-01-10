class Solution:
    def jump(self, nums: List[int]) -> int:
        step=0
        boder=0
        maxpos=0
        n=len(nums)
        for i in range(n-1):
            maxpos=max(maxpos,i+nums[i])
            if i==boder:
                boder=maxpos
                step+=1
        return step

#如果不能保证到达
class Solution:
    def jump(self, nums: List[int]) -> int:
        step=0
        boder=0  # 已建造的桥的右端点
        maxpos=0 # 下一座桥的右端点的最大值
        n=len(nums)
        for i in range(n-1):
            maxpos=max(maxpos,i+nums[i])
            if i==boder:
                if i==maxpos: # 由于next_right = cur_right，这里就代表无法往更远处去了，因此止步于此
                    return -1 # 此时的i也是能到达的最远位置
                boder=maxpos
                step+=1
        return step