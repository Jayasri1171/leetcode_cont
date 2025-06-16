class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans=-1
        for i in range(len(nums)-1):
            ch=nums[i]
            arr=nums[i+1::]
            z=max(arr)
            if(z-nums[i]>ans):
                ans=z-nums[i]
            # print(ans,z,arr)
        if ans==0:
            return -1
        return ans
        