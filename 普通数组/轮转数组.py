class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        if k==0:
            return nums
        nums_1=nums[:n-k]
        nums_2=nums[-k:]
        nums.clear()
        nums.extend(nums_2)
        nums.extend(nums_1)