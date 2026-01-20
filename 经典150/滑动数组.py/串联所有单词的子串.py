from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []
        
        word_len = len(words[0])
        total_len = word_len * len(words)
        target = Counter(words)
        n = len(s)
        ans = []

        # 关键：枚举 word_len 种起始对齐方式
        for start in range(word_len):
            cnt = target.copy()  # 每个起点独立维护计数器
            left = start  # 窗口左边界（单词起始索引）
            
            # right 是当前要加入的单词的右端点（exclusive）
            for right in range(start + word_len, n + 1, word_len):
                # 1. 加入新单词
                in_word = s[right - word_len: right]
                cnt[in_word] -= 1

                # 2. 如果超了（或非法单词），收缩窗口直到合法
                while cnt[in_word] < 0:
                    out_word = s[left: left + word_len]
                    cnt[out_word] += 1
                    left += word_len

                # 3. 检查窗口是否达到目标长度
                if right - left == total_len:
                    ans.append(left)

        return ans
    

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])  # 一个单词的长度
        window_len = word_len * len(words)  # 所有单词的总长度，即窗口大小

        # 目标：窗口中的单词出现次数必须与 target_cnt 完全一致
        target_cnt = Counter(words)

        ans = []
        # 枚举第一个窗口的左端点，做 word_len 次起点不同的滑动窗口
        for start in range(word_len):
            cnt = defaultdict(int)
            overload = 0  # 统计过多的单词个数（包括不在 words 中的单词）
            # 枚举窗口最后一个单词的右开端点
            for right in range(start + word_len, len(s) + 1, word_len):
                # 1. in_word 进入窗口
                in_word = s[right - word_len: right]
                # 下面 cnt[in_word] += 1 后，in_word 的出现次数过多
                if cnt[in_word] == target_cnt[in_word]:
                    overload += 1
                cnt[in_word] += 1

                left = right - window_len  # 窗口第一个单词的左端点
                if left < 0:  # 窗口大小不足 window_len
                    continue

                # 2. 更新答案
                # 如果没有超出 target_cnt 的单词，那么也不会有少于 target_cnt 的单词
                if overload == 0:
                    ans.append(left)

                # 3. 窗口最左边的单词 out_word 离开窗口，为下一轮循环做准备
                out_word = s[left: left + word_len]
                cnt[out_word] -= 1
                if cnt[out_word] == target_cnt[out_word]:
                    overload -= 1

        return ans