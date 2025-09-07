class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans=[]
        if(n==2):
            return [-1,1]
        for i in range(n-1):
            ans.append(i)
        ans.append(-(sum(ans)))
        return ans
        