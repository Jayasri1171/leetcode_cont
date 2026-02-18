class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        z=bin(n)
        z=z[2::]
        chk=z[0]
        for i in range(1,len(z)):
            if chk!=z[i]:
                chk=z[i]
            else:
                return False
        return True