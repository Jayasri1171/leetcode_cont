class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        check=1
        ans=0
        n=len(colors)
        for i in range(1,n+k-2+1):
            if colors[i%n]!=colors[(i-1+n)%n]:
                check+=1
            else:
                check=1
            if check>=k:
                ans+=1
        return ans

        