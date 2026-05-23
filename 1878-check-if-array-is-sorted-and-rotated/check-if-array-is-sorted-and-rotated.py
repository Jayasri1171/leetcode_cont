class Solution:
    def check(self, nums: List[int]) -> bool:
        s=nums[::]
        s.sort()
        for i in range(len(nums)):
            z=nums[i:]+nums[0:i]
            # print(z)
            if(z==s):
                return True
        return False