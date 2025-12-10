class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last={c:i for i,c in enumerate(s)} #找到每个字母的最后一次出现的位置
        start=end=0 #一个区间的开始和结尾的位置index
        res=[] 
        for i,c in enumerate(s): 
            end=max(end,last[c]) #更新当前区间内字母，最远的位置
            if i==end: #如果已经到达了当前区间内字母，最远的位置，就可以完成一次划分
                res.append(end-start+1)
                start=i+1 #下一个区间从当前位置+1开始
        return res