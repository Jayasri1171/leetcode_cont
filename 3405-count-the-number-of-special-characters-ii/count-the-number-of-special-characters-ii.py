class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        d={}
        ans=0
        dd={}
        ddd={}
        for i in word:
            if ord(i)>=65 and ord(i)<=90:
                if i not in dd:
                    dd[i]=1
                    z=ord(i)+32
                    m=chr(z)
                    # print(m)
                    if m in d:
                        ddd[m]=1
                        # print(i)
                        ans+=1
            else:
                if i in ddd:
                    if ddd[i]>=1:
                        ddd[i]-=1
                        ans-=1
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        # print(d,dd,ddd)
        return ans
        