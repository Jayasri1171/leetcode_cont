class Solution:
    def kthCharacter(self, k: int) -> str:
        check='abcdefghijklmnopqrstuvwxyz'
        word=['a']
        while(True):
            if(len(word)>=k):
                return word[k-1]
            s=''
            for i in word:
                s+=chr(ord(i)+1)
            # print(s)
            word+=list(s)
        
            
        