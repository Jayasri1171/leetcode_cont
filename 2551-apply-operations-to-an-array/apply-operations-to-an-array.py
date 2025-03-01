class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i=0
        j=1
        while(j<len(nums)):
            if nums[i]==nums[j]:
                nums[i]=nums[i]*2
                nums[j]=0
                i+=1
                j+=1
            else:
                i+=1
                j+=1
        zerocount=0
        i=0
        while(i<len(nums)):
            if nums[i]==0:
                zerocount+=1
                nums.remove(nums[i])
            else:
                i+=1
            # print(nums)
        return nums+[0]*zerocount
        