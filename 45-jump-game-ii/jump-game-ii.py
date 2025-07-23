class Solution:
    def jump(self, nums: List[int]) -> int:
        far=near=jump=0
        while (far<len(nums)-1):
            maxreach=0
            for j in range(near,far+1):
                maxreach=max(maxreach,nums[j]+j)
            near=far+1
            far=maxreach
            jump+=1
        return jump