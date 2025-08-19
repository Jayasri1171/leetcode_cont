class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        l=[]
        chk=0
        for i in nums:
            if i==0:
                chk+=1
            else:
                l.append(chk)
                chk=0
        l.append(chk)
        ans=0
        for i in l:
            ans+=(i*(i+1))//2
        return ans
        