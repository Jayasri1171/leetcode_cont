class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d=Counter(nums)
        for i in d:
            if d[i]%2!=0:
                return False
        if len(nums)%2==0:
            return True
        return False
        