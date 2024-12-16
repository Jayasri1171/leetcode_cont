class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            z=nums.index(min(nums))
            nums[z]=nums[z]*multiplier
        return nums
        