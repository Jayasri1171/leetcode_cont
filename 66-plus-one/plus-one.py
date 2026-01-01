class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rem=1
        i=len(digits)-1
        while(i>=0):
            if(rem==1):
                if(digits[i]==9):
                    digits[i]=0
                    rem=1
                else:
                    digits[i]+=1
                    rem=0
                    break
            i-=1
        if rem==1:
            digits=[1]+digits
        return digits
        