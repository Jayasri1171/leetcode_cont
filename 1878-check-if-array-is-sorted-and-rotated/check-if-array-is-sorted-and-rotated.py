class Solution:
    def check(self, nums: List[int]) -> bool:
        i=0
        j=len(nums)-1
        ee=nums[::]
        ee.sort()
        if(ee==nums):
            return True
        while(i<j):
            z=nums[0]
            nums=nums[1::]
            nums.append(z)
            ee=nums[::]
            ee.sort()
            if ee==nums:
                return True
            i+=1
        return False