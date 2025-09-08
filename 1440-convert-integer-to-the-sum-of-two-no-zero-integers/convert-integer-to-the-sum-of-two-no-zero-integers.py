class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a=1
        b=n-1
        i=0
        while(True):
            s=list(str(b))
            m=list(str(a))
            if '0' in s:
                a+=1
                b-=1
            elif '0' in m:
                a+=1
                b-=1
            else:
                return [a,b]
            i+=1
        