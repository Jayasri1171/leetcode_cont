class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        lft=[]
        lfttmp=0
        for i in nums:
            lft.append(lfttmp)
            lfttmp+=i
        rft=[0]*len(nums)
        rfttmp=0
        for i in range(len(nums)-1,-1,-1):
            rft[i]=rfttmp
            rfttmp+=nums[i]
        ans=[]
        for i in range(len(nums)):
            ans.append(abs(lft[i]-rft[i]))
        return ans
