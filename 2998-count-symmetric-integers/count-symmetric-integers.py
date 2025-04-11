class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans=0
        for i in range(low,high+1):
            s=str(i)
            if(len(s)%2==0):
                half=len(s)//2
                fir=s[0:half]
                sec=s[half:]
                fircou=0
                seccou=0
                for j in range(half):
                    fircou+=int(fir[j])
                    seccou+=int(sec[j])
                if fircou==seccou:
                    ans+=1
        return ans
        