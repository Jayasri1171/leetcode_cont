class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n=0
        m=len(nums)-1 
        bre=-1
       
        while(n<m):
            k=(n+m)//2
            if nums[k]>=0 and nums[k-1]<0:
                bre=k
                break
            elif nums[k]>0:
                m=k
            elif nums[k]<0:
                n=k
            if min(nums)>=0:
                return len(nums)-nums.count(0)
            if max(nums)<=0:
                return len(nums)-nums.count(0)
            

        if bre==-1:
            0
        neg=len(nums[0:bre])
        pos=len(nums[bre::])-nums.count(0)
        return max(neg,pos)

        