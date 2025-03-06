class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        check=[]
        for i in grid:
            for j in i:
                check.append(j)
        check.sort()
        ans=[]
        for i in check:
            if check.count(i)==2:
                ans.append(i)
                check.remove(i)
                break
        c=1
        m=0
        # print(check)
        for i in range(len(check)):
            if check[i]!=c:
                ans.append(c)
                m=-1
                break
            c+=1
        if m==0:
            ans.append(c)
        return ans
        