class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans=0
        i=0
        n=len(grid)
        m=len(grid[0])
        while(i<n):
            j=0
            while(j<m):
                # print(i,j)
                if(grid[i][j]<0):
                    ans+=m-j
                    # print(ans,m-j,grid[i][j],i,j)
                    break
                j+=1
            i+=1
        return ans
