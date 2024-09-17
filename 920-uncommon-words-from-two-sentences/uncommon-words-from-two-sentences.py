class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        total=s1+' '+s2
        l=[]
        k=total[0]
        for i in range(1,len(total)):
            if total[i]==' ':
                l.append(k)
                k=''
            else:
                k+=total[i]
        l.append(k)
        l.sort()
        p=[]
        for i in range(len(l)):
            if l.count(l[i])==1:
                p.append(l[i])
        return p
        