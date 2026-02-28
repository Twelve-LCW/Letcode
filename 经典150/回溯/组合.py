from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        if n < k or k == 0:  # 补充k=0的边界情况
            return res
        
        def dfs(num, cur: list):
            # 终止条件1：当前组合长度达到k，添加副本到结果
            if len(cur) == k:
                res.append(cur.copy())  # 关键：添加副本而非引用
                return
            # 终止条件2：剩余数字不足以凑够k个，剪枝（优化）
            if len(cur) + (n+1 - num) < k:
                return
            # 遍历从num到n的数字，避免重复组合
            for i in range(num, n + 1):
                cur.append(i)
                dfs(i + 1, cur)  # 下一层从i+1开始，避免重复
                cur.pop()  # 回溯
        
        dfs(1, [])  # 初始从1开始，而非0
        return res