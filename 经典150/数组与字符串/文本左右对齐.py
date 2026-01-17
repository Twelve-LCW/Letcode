class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans=[]
        n=len(words)
        i=0
        while i<n:
            start=i #这一行第一个单词的下标
            sum_len=-1 #第一个单词没有空格，但是后面要统一+1，所以设为-1
            while i<n and sum_len+len(words[i])+1<=maxWidth:
                sum_len+=len(words[i])+1 
                i+=1 #所以最后可能i=n
            
            extra_spaces=maxWidth-sum_len #这一行还未分配的空格数
            gaps=i-start-1 #中间的间距个数

            #特殊情况：一行只有一个单词或者最后一行，多余的空格分配到末尾
            if gaps==0 or i==n:
                row=' '.join(words[start:i])+' '*extra_spaces #末尾补空格
                ans.append(row)
                continue

            #一般情况：把extra_spaces均匀分配到gaps个空格中(靠左的空格更多)
            avg,rem=divmod(extra_spaces,gaps)
            spaces=' '*(avg+1) #均匀分配的空格，+1表示原来的一个
            #前rem个gap多一个空格
            row=(spaces+' ').join(words[start:start+rem+1]) +\
                spaces+(spaces).join(words[start+rem+1:i])
            ans.append(row)
        return ans
