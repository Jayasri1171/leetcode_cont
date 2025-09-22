class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        c=list(d.values())
        g=max(c)
        f=c.count(g)

            
        return f*g
                
        