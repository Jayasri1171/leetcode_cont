class Solution:
    def maximum69Number (self, num: int) -> int:
        z=list(str(num))
        for i in range(len(z)):
            if z[i]=='6':
                z[i]='9'
                break
        s=""
        for i in z:
            s+=i
        return int(s)

        