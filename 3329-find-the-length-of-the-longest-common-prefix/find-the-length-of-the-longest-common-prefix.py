class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        d={}
        for i in range(len(arr1)):
            z=str(arr1[i])
            for j in range(len(z)):
                m=z[0:j+1]
                if m not in d:
                    d[m]=1
        ans=0
        for i in range(len(arr2)):
            z=str(arr2[i])
            for j in range(len(z)):
                m=z[0:j+1]
                if m in d:
                    ans=max(ans,len(m))

        return ans
