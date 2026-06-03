class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=[i]
            else:
                d[nums[i]].append(i)
        for i in range(len(nums)):
            z=target-nums[i]
            if z!=nums[i]:
                if z in d:
                    return [i,d[z][0]]
            else:
                if len(d[z])>1:
                    return d[z][0:2]