class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d={}
        for i in range(len(nums1)):
            if nums1[i][0] not in d:
                d[nums1[i][0]]=nums1[i][1]
            else:
                d[nums1[i][0]]+=nums1[i][1]
        for i in range(len(nums2)):
            if nums2[i][0] not in d:
                d[nums2[i][0]]=nums2[i][1]
            else:
                d[nums2[i][0]]+=nums2[i][1]
        z=dict(sorted(d.items(),key=lambda item:item[0]))
        ans=[]
        for i in z:
            l=[i,z[i]]
            ans.append(l)
        return ans
        
        