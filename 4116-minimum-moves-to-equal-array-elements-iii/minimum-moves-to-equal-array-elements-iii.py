class Solution:
    def minMoves(self, nums: List[int]) -> int:
        z=max(nums)
        ans=0
        for i in nums:
            ans+=z-i
        return ans