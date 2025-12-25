class Solution:
    def maximumHappinessSum(self, hap: List[int], k: int) -> int:
        hap.sort()
        m=0
        c=0
        for i in range(k):
            if(hap[len(hap)-1])-m>=0:
                c+=hap[len(hap)-1]-m
            m+=1
            hap.pop()
        return c




        