class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        i=0
        count=sum(chalk)
        k=k%count
        while(True):
            if chalk[i]>k:
                return i
            else:
                k-=chalk[i]
            if i==len(chalk)-1:
                i=0
            else:
                i+=1
        return 20

        