class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        check=[]
        nums=bin(n)
        nums=nums[2::]
        nums=nums[::-1]
        for i in range(len(nums)):
            if nums[i]=='1':
                check.append(1<<i)
        ans=[]
        for i in range(len(queries)):
            z=1
            m=queries[i]
            for j in range(m[0],m[1]+1):
                z=(z*check[j])%1000000007
            ans.append(z)
        return ans


        