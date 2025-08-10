class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        num = list(str(n))
        num.sort()
        for i in range(0,31):
            z=1<<i
            check=list(str(z))
            check.sort()
            if(check==num):
                return True
        return False


        