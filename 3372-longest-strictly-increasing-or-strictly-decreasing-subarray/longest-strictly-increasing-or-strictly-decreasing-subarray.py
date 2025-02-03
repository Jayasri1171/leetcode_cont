class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans=0
        i=0
        j=len(nums)
        while(i<j-1):
            count=0
            cur=i
            check=0
            if nums[i]<nums[i+1]:
                check=1
            else:
                check=-1
            if check==1:
                cur=i
                count=0
                prev=nums[cur]
                cur=cur+1
                while(cur<j):
                    if nums[cur]>prev:
                        prev=nums[cur]
                        cur+=1
                        count+=1
                    else:
                        break
            elif check==-1:
                cur=i
                count=0
                prev=nums[cur]
                cur=cur+1
                while(cur<j):
                    if nums[cur]<prev:
                        prev=nums[cur]
                        cur+=1
                        count+=1
                    else:
                        break
            if ans<count:
                ans=count
            i+=1
        return ans+1



                

            
        