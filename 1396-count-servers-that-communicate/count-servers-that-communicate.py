class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        count=0
        n=len(grid)
        m=len(grid[0])
        for i in range(n):
            for j in range(m):
                check=0
                if(grid[i][j]==1):
                    for ii in range(n):
                        if grid[ii][j]==1 and ii!=i:
                            check+=1
                            break
                    for jj in range(m):
                        if grid[i][jj]==1 and jj!=j:
                            check+=1
                            break
                    if check!=0:
                        count+=1
        return count    
                    
