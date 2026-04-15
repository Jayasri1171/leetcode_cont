class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        chk=[]
        for i in range(0,len(words)):
            if words[i]==target:
                chk.append(i)
        if chk==[]:
            return -1
        tmp=[]
        for i in chk:
            if i<startIndex:
                tmp.append(startIndex-i)
                tmp.append(i-startIndex+len(words))
            else:
                tmp.append(i-startIndex)
                tmp.append(startIndex+len(words)-i)
        # print(tmp)
        return min(tmp)