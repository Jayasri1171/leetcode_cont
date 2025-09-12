class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vow='aeiou'
        count=0
        for i in s:
            if i in vow:
                count=1
                break
        if count==1:
            return True
        else:
            return False



        