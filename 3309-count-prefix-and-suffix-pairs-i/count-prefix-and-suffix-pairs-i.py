class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count=0
        # words.sort()
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                words[i]=list(words[i])
                words[j]=list(words[j])
                if len(words[j])>=len(words[i]):
                    if words[i]==words[j][0:len(words[i])]:
                        if words[i]==words[j][len(words[j])-len(words[i])::]:
                            count+=1
        return count
        