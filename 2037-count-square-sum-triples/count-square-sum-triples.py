class Solution:
    def countTriples(self, n: int) -> int:
        ans=0
        for i in range(1,n):
            for j in range(i+1,n+1):
                if(sqrt(i*i+j*j)<=n):
                    z=sqrt(i*i+j*j)
                    if(int(z)==z):
                        ans+=1
        return ans*2

        