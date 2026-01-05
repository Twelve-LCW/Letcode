class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0=p1=0 #p1是所有为0和1的位置，p0是所有为0的位置
        for i,x in enumerate(nums):
            nums[i]=2 #所有值都先改成2
            if x<=1: #找到一个小于等于1的数，先把p1位置改为1
                nums[p1]=1
                p1+=1
            if x==0:
                nums[p0]=0
                p0+=1
    
    def sortColors(self, nums: List[int]) -> None:
        p0=p1=0
        for i,x in enumerate(nums):
            if x==1:
                x,nums[p1]=nums[p1],x
                p1+=1
            if x==0:
                x,nums[p0]=nums[p0],x
                if p0<p1:
                    x,nums[p1]=nums[p1],x
                p0+=1
                p1+=1
