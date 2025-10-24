class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        ans=n+1
        while(True):
            z=list(str(ans))
            d={}
            temp=0
            for i in z:
                if i not in d:
                    d[i]=1
                else:
                    d[i]+=1
            for i in d:
                if i!=str(d[i]):
                    temp=-1
            if temp==0:
                return ans
            ans+=1
        return ans
        