class Solution:
    def maxFreqSum(self, s: str) -> int:
        dv={}
        dc={}
        chk='aeiou'
        for i in s:
            if i in chk:
                if i not in dv:
                    dv[i]=1
                else:
                    dv[i]+=1
            else:
                if i in dc:
                    dc[i]+=1
                else:
                    dc[i]=1
        vw=list(dv.values())
        cs=list(dc.values())
        couvv=0
        coucs=0
        if vw!=[]:
            couvv=max(vw)
        if cs!=[]:
            coucs=max(cs)
        return couvv+coucs

        