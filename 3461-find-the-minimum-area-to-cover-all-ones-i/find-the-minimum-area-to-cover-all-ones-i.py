class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        count=0
        minlent=1000
        maxlent=0
        minheig=10000
        maxheig=0
        for i in range(len(grid)):
            m=grid[i]
            for j in range(len(m)):
                if(m[j]==1):
                    if(minheig>i+1):
                        minheig=i+1
                    if(maxheig<i+1):
                        maxheig=i+1
                    if(minlent>j+1):
                        minlent=j+1
                    if(maxlent<j+1):
                        maxlent=j+1
            # print(minheig,minlent,maxheig,maxlent)
        lent=maxlent-minlent+1
        heig=maxheig-minheig+1
        return lent*heig
                
        