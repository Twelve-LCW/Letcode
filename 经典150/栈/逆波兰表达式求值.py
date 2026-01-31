class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        # res=0
        for c in tokens:
            if c not in "+-*/":
                stack.append(int(c))
            else:
                a=stack.pop()
                b=stack.pop()
                if c=="+":
                    stack.append(b+a)
                elif c=="-":
                    stack.append(b-a)
                elif c=="*":
                    stack.append(b*a)
                elif c=="/":
                    stack.append(int(b/a))
        return stack[-1]
