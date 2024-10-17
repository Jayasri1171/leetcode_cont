class Solution:
    def maximumSwap(self, num: int) -> int:
        s=list(str(num))
        l=s[::]
        l.sort()
        l=l[::-1]
        # print(s)
        # print(l)
        for i in range(len(l)):
            if s[i]!=l[i]:
                m=s[i+1::]
                n=max(m)
                q=m.index(n)
                for j in range(len(m)-1,q,-1):
                    if m[j]==n: 
                        q=j
                        break
                
                s[i],s[q+i+1]=s[q+i+1],s[i]
                # print(q,n,m)
                break
        count=0
        for i in s:
            count=count*10+int(i)
        return count
        