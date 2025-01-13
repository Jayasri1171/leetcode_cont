class Solution:
    def minimumLength(self, s: str) -> int:
        s=list(s)
        d={}
        i=0
        count=0
        while(i<len(s)):
            if(s[i] not in d):
                d[s[i]]=1
                count+=1
            else:
                d[s[i]]+=1
                count+=1
                if(d[s[i]]==3):
                    count-=2
                    d[s[i]]=1
            i+=1
        return count
        