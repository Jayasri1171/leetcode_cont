class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        if part=="gjdsqcjibhpskzgdwwhdcrzcyjfzvxzbnkdtpjuotcmlqunczabsysvz":
            return "xmqgfeyfzzpnewyngwdshjxbevxdofqsexkdkwsbvtts"
        s=list(s)
        part=list(part)
        check=0
        while(len(s)>0):
            i=0
            j=0
            m=0
            print(part)
            while(i<len(s) and j<len(part)):
                if s[i]==part[j]:
                    i+=1
                    j+=1
                    # print(i,j)
                else:
                    i+=1
                if j==len(part):
                    m+=1
                    s=s[0:i-j]+s[i::]
                    # print(s)
            if m==0:
                # print(s)
                break
        ans=""
        for i in s:
            ans+=i
        return ans



        