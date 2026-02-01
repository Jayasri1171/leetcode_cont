class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans=nums[0]
        nums.sort()
        if ans!=nums[0]:
            if ans!=nums[1]:
                ans+=nums[0]+nums[1]
            else:
                ans+=nums[0]+nums[2]
        else:    
            ans+=nums[1]+nums[2]
        return ans
        