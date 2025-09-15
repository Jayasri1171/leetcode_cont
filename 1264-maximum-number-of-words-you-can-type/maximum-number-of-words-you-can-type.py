class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        l=text.split(' ')
        ans=len(l)
        for i in l:
            for j in i:
                if j in brokenLetters:
                    ans-=1
                    break
        return ans
        