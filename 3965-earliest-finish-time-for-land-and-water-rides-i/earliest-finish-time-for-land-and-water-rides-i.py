class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        firstland=123456
        for i in range(len(landStartTime)):
            z=landStartTime[i]+landDuration[i]
            firstland=min(firstland,z)
        secondwater=123456
        for i in range(len(waterStartTime)):
            if(waterStartTime[i]<=firstland):
                z=waterDuration[i]
            else:
                z=waterStartTime[i]+waterDuration[i]-firstland
            secondwater=min(secondwater,z)
        firstans=firstland+secondwater
        firstwater=123456
        for i in range(len(waterDuration)):
            z=waterStartTime[i]+waterDuration[i]
            firstwater=min(firstwater,z)
        secondland=123456
        for i in range(len(landDuration)):
            if(landStartTime[i]<=firstwater):
                z=landDuration[i]
            else:
                z=landStartTime[i]+landDuration[i]-firstwater
            secondland=min(secondland,z)
        secondans=firstwater+secondland
        ans=min(firstans,secondans)
        return ans
