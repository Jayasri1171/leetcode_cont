class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans=[]
        for i in nums:
            z=list(str(i))
            tmp=0
            for j in z:
                tmp+=int(j)
            ans.append(tmp)
        ans.sort()
        return ans[0]