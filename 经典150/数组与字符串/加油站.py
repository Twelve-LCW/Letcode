##
# 总结：
# 如果gas和大于cost和就一定能到达。
# 找到欠最多油的index，然后下一个就是出发点。
##
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ans=min_s=s=0 # s 表示油量，min_s 表示最小油量
        for i,(g,c) in enumerate(zip(gas,cost)):
            s+=g-c # 在 i 处加油，然后从 i 到 i+1
            if s<min_s:
                ans=i+1 # 注意 s 减去 c 之后，汽车在 i+1 而不是 i
                min_s=s # 更新最小油量
        # 循环结束后，s 即为 gas 之和减去 cost 之和
        return -1 if s<0 else ans