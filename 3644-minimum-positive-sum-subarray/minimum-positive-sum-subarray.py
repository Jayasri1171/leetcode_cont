class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans=2554525252
        su=0
        ii=l
        while(ii<=r):
            su=0
            for i in range(ii):
                su+=nums[i]
            
            if su>0 and ans>su:
                ans=su
                
            j=ii
            i=0
            while(j<len(nums)):
                su-=nums[i]
                su+=nums[j]
                i+=1
                j+=1
                if(su>0 and su<ans):
                    ans=su
            ii+=1
        # print(ans)
        if ans==2554525252:
            return -1
        return ans

