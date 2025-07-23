class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        i=1
        while(i<len(prices)):
            if(prices[i-1]<prices[i]):
                ans+=prices[i]-prices[i-1]
            i+=1
        return ans
        