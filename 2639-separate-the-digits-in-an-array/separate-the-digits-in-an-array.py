class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            z=nums[i]
            tmp=[]
            while(z):
                s=z%10
                z=z//10
                tmp.append(s)
            tmp=tmp[::-1]
            ans+=tmp
        return ans