from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []  # 存储后序遍历结果
        g = [[] for _ in range(numCourses)]  # 邻接表：存储课程依赖关系
        # 构建图：prerequisites[i] = [a, b] 表示 b 是 a 的前置课程，即 b -> a
        for a, b in prerequisites:
            g[b].append(a)
        
        colors = [0] * numCourses  # 0:未访问 1:访问中 2:已访问
        has_cycle = False  # 标记是否存在环

        def dfs(x: int) -> None:
            nonlocal has_cycle
            if has_cycle:  # 已发现环，提前终止
                return
            colors[x] = 1  # 标记为访问中
            for y in g[x]:  # 遍历所有后继课程
                if colors[y] == 1:  # 发现环（当前节点的后继正在访问中）
                    has_cycle = True
                    return
                if colors[y] == 0:  # 未访问过，递归处理
                    dfs(y)
            colors[x] = 2  # 标记为已访问
            res.append(x)  # 后序遍历：所有依赖处理完后加入结果

        # 遍历所有课程，处理未访问的节点
        for i in range(numCourses):
            if colors[i] == 0 and not has_cycle:
                dfs(i)
        
        # 有环则返回空列表，无环则返回拓扑排序（后序结果反转）
        return [] if has_cycle else res[::-1]