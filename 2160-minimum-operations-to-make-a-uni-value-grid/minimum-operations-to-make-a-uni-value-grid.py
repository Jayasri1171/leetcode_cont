class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        l=[]
        chk=grid[0][0]%x
        for i in grid:
            for j in i:
                if(j%x!=chk):
                    return -1
                l.append(j)
        l.sort()
        z=len(l)//2
        s=l[z]
        ans=0
        for i in l:
            diff=abs(i-s)
            ans+=diff//x
        return ans