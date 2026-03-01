"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
from collections import Counter


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        flat = [num for row in grid for num in row]
        
        # 如果所有数字相同 → 叶子节点
        if len(Counter(flat)) == 1:
            return Node(grid[0][0], True)
        
        # 切分为四个子块
        mid = n // 2
        topLeft = self.construct([row[:mid] for row in grid[:mid]])
        topRight = self.construct([row[mid:] for row in grid[:mid]])
        bottomLeft = self.construct([row[:mid] for row in grid[mid:]])
        bottomRight = self.construct([row[mid:] for row in grid[mid:]])
        
        # 非叶子节点
        return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)