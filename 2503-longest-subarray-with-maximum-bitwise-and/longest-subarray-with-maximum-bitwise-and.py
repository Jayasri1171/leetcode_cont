class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        z=max(nums)
        ans=0
        check=0
        for i in nums:
            if i==z:
                check+=1
            else:
                ans=max(check,ans)
                check=0
        if ans==0:
            return check       
        return ans
        