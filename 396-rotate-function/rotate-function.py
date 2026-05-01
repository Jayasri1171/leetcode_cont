class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        ans=0
        tmp=0
        ttl=0
        for i in range(len(nums)):
            tmp+=i*nums[i]
            ttl+=nums[i]
        ans=tmp
        for i in range(1,len(nums)):
            bst=tmp+ttl-(len(nums)*nums[len(nums)-i])
            ans=max(bst,ans)
            tmp=bst
        return ans