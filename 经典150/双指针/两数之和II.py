class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        sum=0
        while l<r:
            sum=numbers[l]+numbers[r]
            if sum>target:
                r-=1
            elif sum<target:
                l+=1
            else:
                break
        return [l+1,r+1]

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indexes = {}

        for i,x in enumerate(numbers):
            if target-x in indexes:
                return [indexes[target-x]+1, i+1]
            indexes[x] = i