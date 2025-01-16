class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        count1=nums1[0]
        for i in range(1,len(nums1)):
            count1^=nums1[i]
        count2=nums2[0]
        for i in range(1,len(nums2)):
            count2^=nums2[i]
        a=len(nums1)
        b=len(nums2)
        if(a%2==0 and b%2==0):
            return 0
        if(a%2==0 and b%2!=0):
            return count1
        if(b%2==0 and a%2!=0):
            return count2
        return count1^count2
        
        