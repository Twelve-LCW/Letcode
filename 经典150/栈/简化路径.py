class Solution:
    def simplifyPath(self, path: str) -> str:
        path=path.split('/')
        if len(path)==0:
            return '/'
        st=[]
        for c in path:
            if c == '.' or c == ' ' or c == '':
                continue
            elif c=='..':
                if st:
                    st.pop()
            else:
                st.append(c)
        return '/'+'/'.join(st)