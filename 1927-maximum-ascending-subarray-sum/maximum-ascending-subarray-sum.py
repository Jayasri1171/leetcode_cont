class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans=0
        i=0
        j=len(nums)
        while(i<j):
            cur=i
            count=0
            prev=-1
            while(cur<j):
                if nums[cur]>prev:
                    prev=nums[cur]
                    count+=nums[cur]
                    cur+=1
                else:
                    break
            if count>ans:
                ans=count
            i+=1
        return ans