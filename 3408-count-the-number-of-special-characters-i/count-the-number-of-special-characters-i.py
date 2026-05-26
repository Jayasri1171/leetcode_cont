class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        d={}
        for i in word: 
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        ans=0
        word=list(set(word))
        for i in word:
            if ord(i)<=90 and ord(i)>=65:
                z=ord(i)+32
                m=chr(z)
                if m in d:
                    ans+=1
        return ans