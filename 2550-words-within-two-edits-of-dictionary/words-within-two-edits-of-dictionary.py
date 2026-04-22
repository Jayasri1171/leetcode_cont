class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans=[]
        for i in queries:
            for j in dictionary:
                tmp=0
                k=0
                l=0
                while(k<len(i)):
                    if i[k]!=j[l]:
                        tmp+=1
                    k+=1
                    l+=1
                if(tmp<=2):
                    ans.append(i)
                    break
        return ans