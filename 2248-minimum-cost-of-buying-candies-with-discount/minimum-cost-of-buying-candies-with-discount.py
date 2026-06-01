class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        cost=cost[::-1]
        ans=0
        i=0
        while(i<len(cost)-2):
            z=cost[i:i+3]
            ans=ans+z[1]+z[0]
            i+=3
        while(i<len(cost)):
            ans+=cost[i]
            i+=1
        return ans
            