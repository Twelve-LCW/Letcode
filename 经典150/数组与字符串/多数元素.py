class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res=hp=0 #结果和血量
        for num in nums:
            if hp==0: #没有擂主，当前num成为擂主
                res=num
            if res==num:
                hp+=1 #血量加1
            elif num!=res: #不是当前擂主的人，打一架
                hp-=1 #扣一点血
        return res