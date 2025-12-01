class Solution:
    def decodeString(self, s: str) -> str:
        i=0
        def decode():
            nonlocal i
            res=[]
            k=0
            while i <len(s):
                c=s[i]
                i+=1
                if c.isalpha():
                    res.append(c)
                elif c.isdigit():
                    k=k*10+int(c)
                elif c=='[':
                    res.append(decode()*k)
                    k=0
                elif c==']':
                    break
            return ''.join(res)
        return decode()

    def decodeString(self, s: str) -> str:
        stack=[]
        res=''
        k=0
        for c in s:
            if c.isalpha():
                res+=c
            elif c.isdigit():
                k=k*10+int(c)
            elif c=='[':
                stack.append((res,k))
                res=''
                k=0
            elif c==']':
                pre_res,pre_k=stack.pop()
                res=pre_res+res*pre_k
        return res