from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bfs=deque()
        bfs.append((startGene,0))
        bankset=set(bank)
        while bfs:
            gene,step=bfs.popleft()
            if gene==endGene:
                return step
            for i in range(8):
                for x in "ACGT":
                    newGene=gene[:i]+x+gene[i+1:]
                    if newGene in bankset and newGene!=gene:
                        bfs.append((newGene,step+1))
                        bankset.remove(newGene)
        return -1
    

import collections
from typing import List

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        """
        计算从起始基因序列到目标基因序列所需的最小突变次数
        :param start: 起始基因序列 (长度为8的字符串，仅包含A/C/G/T)
        :param end: 目标基因序列
        :param bank: 基因库，包含所有有效的中间突变序列
        :return: 最小突变次数，无法达到则返回-1
        """
        # 如果目标基因不在基因库中，直接返回-1（提前剪枝）
        if end not in bank:
            return -1
        
        # 将基因库转为集合，提升查询效率
        bank_set = set(bank)
        # BFS队列，存储(当前基因, 已突变次数)
        queue = collections.deque([(start, 0)])
        # 记录已访问的基因，避免重复处理
        visited = set([start])
        
        # 基因的四种可能碱基
        nucleotides = ['A', 'C', 'G', 'T']
        
        while queue:
            current_gene, steps = queue.popleft()
            
            # 遍历当前基因的每一个位置
            for i in range(8):
                # 尝试将当前位置替换为四种不同的碱基
                for char in nucleotides:
                    # 跳过和原碱基相同的情况
                    if current_gene[i] == char:
                        continue
                    
                    # 生成新的基因序列
                    new_gene = current_gene[:i] + char + current_gene[i+1:]
                    
                    # 如果新基因是目标基因，直接返回步数+1
                    if new_gene == end:
                        return steps + 1
                    
                    # 如果新基因在基因库中且未被访问过
                    if new_gene in bank_set and new_gene not in visited:
                        visited.add(new_gene)
                        queue.append((new_gene, steps + 1))
        
        # 无法到达目标基因
        return -1