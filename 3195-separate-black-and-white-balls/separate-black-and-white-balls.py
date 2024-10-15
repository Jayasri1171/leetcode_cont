class Solution:
    def minimumSteps(self, s: str) -> int:
        count=0
        onecount=0
        zerocount=0
        for i in s:
            if i=='0':
                count+=onecount
            else:
                onecount+=1
        return count     