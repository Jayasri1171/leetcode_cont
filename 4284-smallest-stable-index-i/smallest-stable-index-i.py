class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        for i in range(len(nums)):
            mx=max(nums[0:i+1])
            mn=min(nums[i:n])
            z=mx-mn
            if z<=k:
                return i
        return -1