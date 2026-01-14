class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sps=s.split(' ')
        res=0
        for sp in sps:
            if len(sp)>0:
                res=len(sp)
        return res

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1  # 从字符串末尾开始
        while s[i] == ' ':  # 跳过末尾的空格
            i -= 1

        j = i - 1  # 从最后一个非空格字符的前一个字符开始往前找
        while j >= 0 and s[j] != ' ':  # 直到遇到空格或到达字符串开头
            j -= 1

        return i - j  # 最后一个单词的长度 = 最后一个字母索引 - 前一个空格索引
