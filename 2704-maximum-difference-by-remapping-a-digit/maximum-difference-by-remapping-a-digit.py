class Solution:
    def minMaxDifference(self, num: int) -> int:
        s=str(num)
        max=0
        min=0
        ch='hj'
        for i in s:
            if i!='9' and ch=='hj':
                ch=i
                max=max*10+9
            elif ch!='hj' and i==ch:
                max=max*10+9
            else:
                max=max*10+int(i)
        vj='kj'
        for i in s:
            if i!=0 and vj=='kj':
                vj=i
                min=min*10+0
            elif vj!='kj' and i==vj:
                min=min*10+0
            else:
                min=min*10+int(i)
        # print(min,max)
        return max-min



        