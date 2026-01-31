class Solution(object):
    def calculate(self, s):
        res, num, sign = 0, 0, 1 # 初始化当前结果、当前处理的数字和当前符号
        stack = []  # 用于存储每个括号前的计算结果和符号

        for c in s:
            if c.isdigit():
                # 处理多位数的情况
                num = 10 * num + int(c)
            elif c == "+" or c == "-":
                # 遇到符号，更新当前结果，并重置num以用于下一个数字的计算
                # 使用之前的符号计算之前的数字
                res += sign * num
                num = 0  # 重置num
                # 设置新的符号
                sign = 1 if c == "+" else -1
            elif c == "(":
                # 遇到左括号时，将当前的计算结果和符号入栈
                # 然后重置res和sign以计算括号内的表达式
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                # 遇到右括号时，计算括号内的表达式的结果
                # 并将其与栈顶的符号和之前的结果相加
                res += sign * num
                num = 0
                # 用括号前的符号乘以括号内的结果
                res *= stack.pop()
                # 然后加上括号前的结果
                res += stack.pop()
        # 对表达式最后的数字进行计算
        res += sign * num
        return res
    

class Solution:
    def calculate(self, s: str) -> int:
        ops = [1]
        sign = 1

        ret = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = ops[-1]
                i += 1
            elif s[i] == '-':
                sign = -ops[-1]
                i += 1
            elif s[i] == '(':
                ops.append(sign)
                i += 1
            elif s[i] == ')':
                ops.pop()
                i += 1
            else:
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + ord(s[i]) - ord('0')
                    i += 1
                ret += num * sign
        return ret