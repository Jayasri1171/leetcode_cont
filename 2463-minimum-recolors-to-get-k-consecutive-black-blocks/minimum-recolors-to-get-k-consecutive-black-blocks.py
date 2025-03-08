class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        blocks=list(blocks)
        # print(len(blocks))
        slid = blocks[0:k]
        ans = slid.count('W')
        i=0
        j=k
        while(j<=len(blocks)):
            slid=blocks[i:j]
            minn=slid.count('W')
            if minn<ans:
                ans=minn
            i+=1
            j+=1
        return ans



        