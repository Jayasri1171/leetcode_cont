class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        originalsize=len(rolls)
        originalsum=sum(rolls)
        total=originalsize+n
        mean=mean*total
        diff=mean-originalsum
        if(diff>n*6 or diff<0):
            return []
        returnarray=[]
        z=diff//n
        if (z==0 or z>6):
            return []
        for i in range(n):
            returnarray.append(z)
        rem=diff-z*n
        print(rem)
        for i in range(n):
            if rem>0:
                if returnarray[i]<6:
                    if rem<6:
                        z=(6-returnarray[i])
                        if rem>z:
                            m=z
                        else:
                            m=rem
                    else:
                        m=6-returnarray[i]
                    returnarray[i]+=m
                    rem-=m
            else:
                break
            
        return returnarray



        