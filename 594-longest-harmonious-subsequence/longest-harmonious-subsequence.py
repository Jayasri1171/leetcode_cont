class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ans=0
        m=list(set(nums))
        for i in range(len(m)):
            if m[i]+1 not in m:
                continue
            else:
                z=nums.count(m[i])+nums.count(m[i]+1)
                ans=max(ans,z)
        return ans
        