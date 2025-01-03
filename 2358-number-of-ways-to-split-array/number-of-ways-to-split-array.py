class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        l=[]
        summ=0
        for i in range(len(nums)):
            summ+=nums[i]
            l.append(summ)
        count=0
        # print(l)
        for j in range(len(nums)-1):
            m=l[j]
            n=l[len(l)-1]-m
            # print(m,n)
            if m>=n:
                # print(m,n)
                count+=1
        return count
        
        