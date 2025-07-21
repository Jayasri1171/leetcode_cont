class Solution:
    def makeFancyString(self, s: str) -> str:
        a=""
        for i in range(1,len(s)-1):
            if s[i-1]==s[i]==s[i+1]:
                continue
            else:
                a+=s[i-1]
        a+=s[len(s)-2:len(s):]
        
        return a
        