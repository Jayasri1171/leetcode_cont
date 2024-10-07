class Solution:
    def minLength(self, s: str) -> int:
        next=0
        while(next==0):
            count=0
            i=0
            j=1
            while(j<len(s)):
                if s[i]=='A' and s[j]=='B':
                    s=s[0:i]+s[j+1:len(s)]
                    count+=1
                elif s[i]=='C' and s[j]=='D':
                    s=s[0:i]+s[j+1:len(s)]
                    count+=1
                else:
                    i+=1
                    j+=1
            if count==0:
                next=1
            else:
                next=0
        return len(s)
        