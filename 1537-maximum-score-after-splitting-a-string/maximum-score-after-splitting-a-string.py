class Solution:
    def maxScore(self, s: str) -> int:
        count=0
        for i in range(1,len(s)):
            a=s[0:i]
            b=s[i::]
            k=a.count('0')
            m=b.count('1')
            # print(a,b,k,m)
            if count<k+m:
                count=k+m
        return count
