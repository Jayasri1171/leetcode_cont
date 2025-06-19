class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if(n<=1):
            return s
        def sri(l,r):
            while(l>=0 and r<n and s[l]==s[r]):
                l-=1
                r+=1
            return s[l+1:r]
        max_str=s[0]
        for i in range(len(s)-1):
            oddstr=sri(i,i)
            evenstr=sri(i,i+1)
            # print(oddstr)
            # print(evenstr)
            if(len(oddstr)>len(max_str)):
                max_str=oddstr
            if(len(evenstr)>len(max_str)):
                max_str=evenstr
        return max_str

        