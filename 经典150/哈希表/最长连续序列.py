class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len=0
        num_set=set(nums)
        for num in num_set:
            if num-1 not in num_set:
                current_num=num
                current_len=1

                while current_num+1 in num_set:
                    current_num+=1
                    current_len+=1
                
                max_len=max(max_len,current_len)
        return max_len


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums_set = set(nums)

        for num in nums_set:
            if num-1 in nums_set:
                continue

            cur_num = num
            while cur_num+1 in nums_set:
                cur_num += 1
            res = max(res, cur_num-num+1)

        return res