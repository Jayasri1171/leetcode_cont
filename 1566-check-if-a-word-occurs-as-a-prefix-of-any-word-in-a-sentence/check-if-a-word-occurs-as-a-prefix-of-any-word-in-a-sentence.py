class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l=list(sentence.split( ))
        for i in range(len(l)):
            j=0
            k=0
            s=l[i]
            while(j<len(s) and k<len(searchWord)):
                if searchWord[k]!=s[j]:
                    break
                j+=1
                k+=1
            if k==len(searchWord):
                return i+1
        return -1


        