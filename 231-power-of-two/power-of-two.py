class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        else:
            s=0
            while(n):
                if (n&1):
                    s=s+1
                n=n>>1
            if s==1:
                return True
            else:
                return False
