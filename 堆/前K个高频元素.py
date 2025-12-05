from collections import Counter, defaultdict
import random


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 统计频率
        nums_cnt=Counter(nums)
        # max_cnt=max(nums_cnt.values())

        # defaultdict(list)：key 是频率，value 是所有出现该频率的数字
        buckets = defaultdict(list)
        for x, c in nums_cnt.items():
            buckets[c].append(x)
        
        res=[]
        # 从最大频率 max(cnt.values()) 开始倒序找
        for bucket in range(max(nums_cnt.values()), 0, -1):
            res+=buckets[bucket]
            if len(res)>=k:
                return res
            
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #统计频率
        count=Counter(nums)
        #转成数组
        num_cnt=list(count.items())
        #快排，找Topk
        topks=self.findtopk(num_cnt,k,0,len(num_cnt)-1)
        return [item[0] for item in topks]

    def findtopk(self,num_cnt,k,low,high):
        #随机找base
        pivot=random.randint(low,high)
        #基准放在第一位
        num_cnt[low],num_cnt[pivot]=num_cnt[pivot],num_cnt[low]
        base=num_cnt[low][1]
        i=low
        #比基准大的往前放（Topk）
        for j in range(low+1,high+1):
            if num_cnt[j][1]>base:
                num_cnt[i+1],num_cnt[j]=num_cnt[j],num_cnt[i+1]
                i+=1
        #把基准放回中间，左边的比它大、右边的比它小
        num_cnt[low],num_cnt[i]=num_cnt[i],num_cnt[low]
        #如果左边+基准正好是k个，找到了Topk
        if i==k-1:
            return num_cnt[:k]
        #如果左边比k个多，还得在左边找出k个最大的
        elif i>k-1:
            return self.findtopk(num_cnt,k,low,i-1)
        #如果左边比k个少，还得去右边找k-i个
        else:
            return self.findtopk(num_cnt,k,i+1,high)