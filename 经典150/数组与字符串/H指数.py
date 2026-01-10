class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h=0
        for i,citation in enumerate(citations):
            if citation>=i+1: #如果当前论文引用量大于当前排序，即h最高为i+1
                h=i+1
            else:
                break
        return h 

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = [0] * (n + 1) #统计引用数为i的论文数
        
        for c in citations:
            if c >= n:
                count[n] += 1 #h不超过n，所以超过n的都记在n，有几篇
            else:
                count[c] += 1
        
        total = 0
        for i in range(n, -1, -1):
            total += count[i] #倒序循环，所以到了i意味着前面>i的论文数有多少
            if total >= i: #如果>=i ，一个从小到大，一个从大到小
                return i
        return 0