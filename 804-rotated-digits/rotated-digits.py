class Solution:
    def rotatedDigits(self, n: int) -> int:
        ans=0
        vld=['2','5','6','9']
        invld=['3','4','7']
        for i in range(1,n+1):
            z=str(i)
            tmp=0
            tmp1=0
            for j in z:
                if j in vld:
                    tmp=1
                elif j in invld:
                    tmp1=1
            if tmp==1 and tmp1!=1:
                ans+=1
        return ans