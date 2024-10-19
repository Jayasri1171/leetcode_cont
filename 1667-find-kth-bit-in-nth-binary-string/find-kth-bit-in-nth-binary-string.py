class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s="0"
        for i in range(1,n):
            z=list(s)
            for j in range(len(z)):
                if z[j]=='0':
                    z[j]='1'
                else:
                    z[j]='0'
            z=z[::-1]
            m=""
            for q in z:
                m+=q

            s+='1'+m
        # print(s)
        return s[k-1]
