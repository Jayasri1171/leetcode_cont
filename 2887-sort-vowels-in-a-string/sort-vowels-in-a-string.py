class Solution:
    def sortVowels(self, s: str) -> str:
        chk='AEIOUaeiou'
        chk=list(chk)
        ans=[]
        for i in s:
            if i in chk:
                ans.append(i)
        ans.sort()
        # print(ans)
        rtu=""
        j=0
        for i in s:
            if i in chk:
                rtu+=ans[j]
                j+=1
            else:
                rtu+=i

        return rtu
        