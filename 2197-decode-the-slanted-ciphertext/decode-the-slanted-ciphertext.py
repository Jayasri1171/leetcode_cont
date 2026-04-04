class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        col=len(encodedText)//rows
        print(col)
        ans=""
        i=0
        while(i<col):
            j=i
            while(j<len(encodedText)):
                ans+=encodedText[j]
                j+=col+1
            i+=1
        ans=ans[::-1]
        # print(ans)
        for ii in range(len(ans)):
            # print(ii)
            if ans[ii]!=" ":
                ans=ans[ii:]
                break
        ans=ans[::-1]
        return ans
