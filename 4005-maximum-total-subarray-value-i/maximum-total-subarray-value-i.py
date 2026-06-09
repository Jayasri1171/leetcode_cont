class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        ans=0
        maxva=max(nums)
        minva=min(nums)
        ans=(maxva-minva)*k
        return ans