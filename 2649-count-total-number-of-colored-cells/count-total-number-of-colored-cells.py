class Solution:
    def coloredCells(self, n: int) -> int:
        ans=1
        if n==1:
            return 1
        for i in range(1,n):
            ans+=4*i
        return ans


        