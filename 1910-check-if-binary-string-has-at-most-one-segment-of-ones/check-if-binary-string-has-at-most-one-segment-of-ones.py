class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        z=0
        for i in s:
            if i=='0':
                z=1
            if z==1 and i=='1':
                return False
        return True