class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans=1
        s=word[0]
        for i in range(1,len(word)):
            if word[i]==s:
                ans+=1
            s=word[i]
        return ans

        