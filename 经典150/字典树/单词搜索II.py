from typing import List  # 补充必要的导入

class TrieNode:
    def __init__(self):
        self.children = {}  # 键是字符，值是 TrieNode
        self.word = None    # 如果是单词结尾，这里存储完整单词；否则为 None

class Solution:
    # 修复：添加 self 参数，使其成为合法的类方法
    def build_trie(self, words):
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = word  # 在单词结尾节点存储单词本身
        return root
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words:  # 补充 board[0] 判空，避免n=len(board[0])报错
            return []
        
        root = self.build_trie(words)
        m = len(board)
        n = len(board[0])
        result = set()  # 用集合去重
        # 修复：创建 visited 矩阵代替修改原始 board，避免副作用
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        def dfs(i, j, node):
            # 越界检查
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            # 已访问过，直接返回
            if visited[i][j]:
                return
            
            c = board[i][j]
            # 如果当前字符不在字典树的当前节点中，剪枝
            if c not in node.children:
                return
            
            # 标记为已访问（替代修改原始board）
            visited[i][j] = True
            
            # 进入下一个节点
            next_node = node.children[c]
            # 如果这个节点是单词结尾，就把单词加入结果
            if next_node.word:
                result.add(next_node.word)
            
            # 向四个方向递归
            dfs(i+1, j, next_node)
            dfs(i-1, j, next_node)
            dfs(i, j+1, next_node)
            dfs(i, j-1, next_node)
            
            # 回溯，取消标记
            visited[i][j] = False
        
        # 遍历每个单元格作为起点
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        
        # 转列表返回，顺序不影响题目判题
        return list(result)