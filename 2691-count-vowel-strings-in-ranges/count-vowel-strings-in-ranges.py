class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        l=[]
        qq='aeiou'
        for i in words:
            s=list(i)
            if s[0] in qq and s[len(s)-1] in qq:
                l.append(1)
            else:
                l.append(0)
        ans=[]
        check=[]
        summ=0
        for i in l:
            summ+=i
            check.append(summ)
        for i in range(len(queries)):
            aa=queries[i][0]
            bb=queries[i][1]
            if aa!=0:
                ans.append(check[bb]-check[aa-1])
            else:
                ans.append(check[bb])
        return ans

        