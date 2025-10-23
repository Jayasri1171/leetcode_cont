class Solution:
    def hasSameDigits(self, s: str) -> bool:
        i=0
        li=list(s)
        while(len(li)>2):
            q=[]
            for i in range(len(li)-1):
                q.append((int(li[i])+int(li[i+1]))%10)
            li=q
        if(li[0]==li[1]):
            return True
        return False
        