class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]
        for i in range(2,numRows+1):
            l=[]
            z=ans[i-2]
            for j in range(i):
                if j==0 or j==i-1:
                    l.append(1)
                else:
                    l.append(z[j-1]+z[j])
            # print(l)
            ans.append(l)
        return ans
        