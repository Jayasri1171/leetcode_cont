class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            z=nums[i]%2
            y=nums[i+1]%2
            if z==y:
                return False
        return True
        