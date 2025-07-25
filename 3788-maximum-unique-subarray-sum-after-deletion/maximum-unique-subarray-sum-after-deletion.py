class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums=list(set(nums))
        ans=0
        for i in nums:
            if i>0:
                ans+=i
        if ans==0:
            return max(nums)
        return ans
            

        