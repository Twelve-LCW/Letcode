class Node:
    __slots__ = 'son', 'end'  # 限制属性，节省内存

    def __init__(self):
        self.son = {}  # 存储子节点，key: 字符，value: Node实例
        self.end = False  # 标记是否是单词的结束位置

class WordDictionary:

    def __init__(self):
        self.root = Node()  # 字典树的根节点（空节点）

    def addWord(self, word: str) -> None:
        """添加一个单词到字典中"""
        cur = self.root
        for c in word:
            if c not in cur.son:
                cur.son[c] = Node()  # 不存在则创建新节点
            cur = cur.son[c]  # 移动到子节点
        cur.end = True  # 标记单词结束

    def search(self, word: str) -> bool:
        """搜索单词，支持通配符.匹配任意单个字符"""
        return self.dfs(word, 0, self.root)
    
    def dfs(self, word, index, root):
        """深度优先搜索辅助函数"""
        # 递归终止条件1：节点为空（路径不存在）
        if root is None:
            return False
        # 递归终止条件2：遍历完所有字符，检查是否是单词结尾
        if len(word) == index:
            return root.end
        
        current_char = word[index]
        # 情况1：当前字符不是通配符，精准匹配
        if current_char != '.':
            if current_char not in root.son:
                return False
            # 传入的是 root.son[current_char]（Node对象），而非字符本身
            return self.dfs(word, index + 1, root.son[current_char])
        # 情况2：当前字符是通配符，遍历所有子节点递归
        else:
            for c in root.son:
                if self.dfs(word, index + 1, root.son[c]):
                    return True
        # 所有子节点都匹配失败
        return False