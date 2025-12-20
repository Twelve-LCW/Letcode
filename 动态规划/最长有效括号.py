class Solution:
    #栈的解法
    #拆炸弹，左括号是炸弹
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        res=0
        n=len(s)
        for i,ch in enumerate(s):
            if ch=='(': #炸弹
                stack.append(i) #要拆的炸弹
            elif len(stack)>1 and ch==')': #拆弹器，并且有要拆的炸弹
                stack.pop()
                res=max(res,i-stack[-1]) # 右端点为 i 时，左端点最小是 stk[-1] + 1
            else: #有拆弹器，但是没有要拆的炸弹，把红线前移
                stack[0]=i
        return res
    #空间优化
    def solve(self, s: Iterable[str], left_ch: str) -> int:
        left=right=res=0
        for ch in s:
            if ch==left_ch: #炸弹
                left+=1
            else:
                right+=1
            if left<right:#拆弹太多，ch变红线，重新计数
                left=right=0
            elif left==right: #正好可以拆
                res=max(res,right*2)
        return res
    def longestValidParentheses(self, s: str) -> int:
        #因为可能出现，炸弹多余拆弹器的情况，所以反转一下，再计算
        return max(self.solve(s,'('),self.solve(reversed(s),')')) #反转过后，要把)当作炸弹
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)
        dp = [0] * n
        maxans = 0

        for i in range(1, n):
            if s[i] == ')':
                # 情况1: ...()
                if s[i - 1] == '(':
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                # 情况2: ...))
                else:
                    # 找到与当前 ')' 匹配的可能位置
                    prev = i - dp[i - 1] - 1  # 这是潜在匹配 '(' 的位置
                    if prev >= 0 and s[prev] == '(':
                        # 当前长度 = 内部已匹配长度 + 2 + 前面挨着的有效长度
                        dp[i] = dp[i - 1] + 2
                        if prev - 1 >= 0:
                            dp[i] += dp[prev - 1]
                maxans = max(maxans, dp[i])
        
        return maxans
