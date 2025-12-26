class Solution:
    def bestClosingTime(self, customers: str) -> int:
        be={'Y':0,'N':0}
        af={'Y':0,'N':0}
        for i in range(len(customers)):
            af[customers[i]]+=1
        ans= af['Y']
        rt=0
        for i in range(len(customers)):
            af[customers[i]]-=1
            be[customers[i]]+=1
            z=af['Y']+be['N']
            if z<ans:
                ans=z
                rt=i+1
        return rt