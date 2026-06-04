class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans=0
        i=num1
        j=num2
        while(i<=j):
            if(i<=100):
                i+=1
                continue
            s=str(i)
            for k in range(1,len(s)-1):
                prev=int(s[k-1])
                nxt=int(s[k+1])
                z=int(s[k])
                if(z<prev and z<nxt):
                    ans+=1
                if(z>prev and z>nxt):
                    ans+=1
            i+=1
        return ans