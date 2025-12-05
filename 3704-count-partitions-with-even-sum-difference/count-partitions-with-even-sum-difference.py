class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)-1):
            z=sum(nums[0:i+1])
            x=sum(nums[i+1::])
            if(abs(z-x)%2==0):
                ans+=1
        return ans