class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i=0
        j=0
        d=""
        check=0
        while(i<len(s)):
            if check==0 and i==spaces[j]:
                d+=" "
                j+=1
                if j==len(spaces):
                    check=1
            else:
                d+=s[i]
                i+=1
        return d


        