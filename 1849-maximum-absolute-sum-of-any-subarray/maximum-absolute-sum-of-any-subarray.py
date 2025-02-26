class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr=nums[0]
        maxsum=nums[0]
        for i in range(1,len(nums)):
            curr=max(curr+nums[i],nums[i])
            maxsum=max(curr,maxsum)
        curr=nums[0]
        minsum=nums[0]
        for i in range(1,len(nums)):
            curr=min(curr+nums[i],nums[i])
            minsum=min(curr,minsum)
        return max(maxsum,abs(minsum))
        