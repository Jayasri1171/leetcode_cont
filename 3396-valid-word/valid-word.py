class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        check='qwertyuioplkjhgfdsazxcvbnmMNBVCXZASDFGHJKLPOIUYTREWQ1234567890'
        voww='AEIOUaeiou'
        consoo='QWRTYPSDFGHJKLMNBVCXZqwrtypsdfghjklmnbvcxz'
        vo=0
        co=0
        for i in word:
            if i not in check:
                return False
            if i in voww:
                vo+=1
            if i in consoo:
                co+=1
        # print(vo,co)
        if vo==0 or co==0:
            return False    
        return True
        