class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans=0
        chk=0
        for i in dimensions:
            s=i
            tmp = (s[0]*s[0]+s[1]*s[1])**0.5
            if(tmp>chk):
                chk=tmp
                ans=s[0]*s[1]
            if(tmp==chk):
                ans=max(ans,s[0]*s[1])
        return ans
        