class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i=1
        while(i<len(words)):
            one=list(words[i-1])
            two=list(words[i])
            one.sort()
            two.sort()
            if one!=two:
                i+=1
            else:
                words=words[0:i]+words[i+1:]
        return words
